# -*- coding: utf-8 -*-
# Update: October 20, 2022
import argparse
import datetime
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Usage example: python PaPhyML.py -f test.fas -a mafft -t raxmlHPC -n")
    parser.add_argument('-f', type=str, help="Add a biological sequence file with FASTA format [required]",
                        default="test.fas")
    parser.add_argument('-a', type=str, help="Select a multiple sequence alignment software [default=mafft]",
                        default="halign", choices=["halign", "mafft", "wmsa", "muscle"])
    parser.add_argument('-t', type=str, help="Select a phylogenetic tree software [default = raxml]",
                        default="raxmlHPC", choices=["raxmlHPC", "phyml", "fasttree", "iqtree"])
    parser.add_argument('-n', required=False, help="The input FASTA file is nucleotide sequence", action="store_true")
    parser.add_argument('-p', required=False, help="The input FASTA file is protein sequence", action="store_true")
    args = parser.parse_args()

    final_output_folder = os.path.join(os.getcwd(), "output")
    if not os.path.exists(final_output_folder):
        os.makedirs(final_output_folder)

    current_time = datetime.datetime.now().strftime('%b%d_%H-%M-%S')

    args = parser.parse_args()
    data_file_path = args.f

    step_1_params = args.a
    step_4_params = args.t

    prefix = ""
    if args.n:
        prefix = "nucleotide"
    elif args.p:
        prefix = "protein"
    # command_test = "dir"
    # command_test_return = os.popen(command_test, 'r', -1)
    # print(command_test_return.read())

    output_dir = prefix + "_" + current_time + "_" + step_4_params + "_output"

    if step_4_params == "raxmlHPC":
        final_output_folder = os.path.join(final_output_folder, "raxml_output", output_dir)
    elif step_4_params == "phyml":
        final_output_folder = os.path.join(final_output_folder, "phyml_output", output_dir)
    elif step_4_params == "fasttree":
        final_output_folder = os.path.join(final_output_folder, "fasttree_output", output_dir)
    elif step_4_params == "iqtree":
        final_output_folder = os.path.join(final_output_folder, "iqtree_output", output_dir)
    else:
        print("The param of Step4 is wrong!")
    if not os.path.exists(final_output_folder):
        os.makedirs(final_output_folder)

    ######################################step1######################################
    step_1_output_path = ""

    if step_1_params == "mafft":
        step_1_output_path = os.path.join(final_output_folder, "seq_alignment.fasta")
        step_1_command = "mafft " + data_file_path + " > " + step_1_output_path
        step_1_return = os.popen(step_1_command)
        print("Step1 output:")
        print(step_1_return.read())

    elif step_1_params == "halign":
        step_1_output_path = os.path.join(final_output_folder, "seq_alignment.fasta")
        step_1_command = "halign" + " -o " + step_1_output_path + " " + data_file_path
        step_1_return = os.popen(step_1_command, 'r', -1)
        print("Step1 output:")
        print(step_1_return.read())

    elif step_1_params == "wmsa":
        step_1_output_path = os.path.join(final_output_folder, "seq_alignment.fasta")
        step_1_command = "wmsa -i " + data_file_path + " -o " + step_1_output_path + " -T 2 -c 0.9"
        step_1_return = os.popen(step_1_command, 'r', -1)
        print("Step1 output:")
        print(step_1_return.read())

    elif step_1_params == "muscle":
        step_1_output_path = os.path.join(final_output_folder, "seq_alignment.fasta")
        step_1_command = "muscle -align " + data_file_path + " -output " + step_1_output_path
        step_1_return = os.popen(step_1_command, 'r', -1)
        print("Step1 output:")
        print(step_1_return.read())
        pass
    else:
        print("The param of Step1 is wrong!")

    ######################################step2######################################
    tmp_file_path = os.path.join(final_output_folder, "seq_alignment.phy.tmp")
    step_2_command_1_shell_path = os.path.join(final_output_folder, "step2_command_1.shell")
    step_2_command_1_return = os.popen("touch " + step_2_command_1_shell_path)
    step_2_command_1 = r"cat " + step_1_output_path + r" |tr '\n' '\t'|sed 's/>/\n/g' |sed 's/\t/      /'|sed 's/\t//g'| awk 'NF > 0' > " + tmp_file_path
    with open(step_2_command_1_shell_path, "w") as f:
        f.write("#!/bin/bash\n")
        f.write(step_2_command_1)
    step_2_command_1_return = os.popen("bash " + step_2_command_1_shell_path)
    print("Step2 part1 output:")
    print(step_2_command_1_return.read())

    step_2_command_2_shell_path = os.path.join(final_output_folder, "step2_command_2.shell")
    step_2_command_2_return = os.popen("touch " + step_2_command_2_shell_path)
    step_2_out_path = os.path.join(final_output_folder, "seq_alignment.phy")
    step_2_command_2 = r"awk '{print " + '"'+'  "'+'NR"'+'  "'+"length($2)}' " + tmp_file_path + "|tail -n 1 | cat -  " + tmp_file_path + " > " + step_2_out_path
    with open(step_2_command_2_shell_path, "w") as f:
        f.write("#!/bin/bash\n")
        f.write(step_2_command_2)
    step_2_command_2_return = os.popen("bash " + step_2_command_2_shell_path)
    print("Step2 part1 output:")
    print(step_2_command_2_return.read())

    ######################################step3######################################
    step_3_out_path = os.path.join(final_output_folder, "seq_alignment_trimmed.phy")
    step_3_out_path_for_fasttree = os.path.join(final_output_folder, "seq_alignment.phy")  # Alignment file for fasttree software
    step_3_command = r" trimal -nogaps -in " + step_2_out_path + " -out " + step_3_out_path + " -automated1 "
    step_3_command_return = os.popen(step_3_command)
    print("Step3 output:")
    print(step_3_command_return.read())

    ######################################step4######################################
    if not args.n and not args.p:
        print("Either N or P has to be selected")

    step_4_command = ""
    if step_4_params == "raxmlHPC":
        if args.n:
            step_4_command = step_4_params + " -f a -x 123456 -p 123456 -s " + step_3_out_path + " -m GTRGAMMA -N 1000 -T 20 -n txt " + " -w " + final_output_folder
        elif args.p:
            step_4_command = step_4_params + " -f a -x 123456 -p 123456 -s " + step_3_out_path + " -m PROTGAMMALGX -N 1000 -T 20 -n txt " + " -w " + final_output_folder
        print(step_4_command)
    elif step_4_params == "phyml":
        if args.n:
            step_4_command = step_4_params + " -i " + step_3_out_path + " -d nt -b 1000 -m HKY85 "
        elif args.p:
            step_4_command = step_4_params + " -i " + step_3_out_path + " -d aa -b 1000 -m LG "

    elif step_4_params == "fasttree":
        fasttree_ouptput = "fasttree_result.txt"
        if args.n:
            step_4_command = step_4_params + " -nt -gtr " + step_3_out_path_for_fasttree + " > " + os.path.join(
                final_output_folder, fasttree_ouptput)
        elif args.p:
            step_4_command = step_4_params + " -nt " + step_3_out_path_for_fasttree + " > " + os.path.join(
                final_output_folder, fasttree_ouptput)

    elif step_4_params == "iqtree":
        if args.n:
            step_4_command = step_4_params + " -s " + step_3_out_path + " -mset HKY -m MFP -T AUTO"
        elif args.p:
            step_4_command = step_4_params + " -s " + step_3_out_path + " -mset LG -mfreq FU -m MFP -T AUTO"
    else:
        print("The param of Step4 is wrong!")
    step_4_return = os.popen(step_4_command)
    print("Step4 output:")
    print(step_4_return.read())
