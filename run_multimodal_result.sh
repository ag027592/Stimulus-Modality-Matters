#!/bin/bash

stage=$1
upstream=$2

corpus=CREMAD

folder_list1=(fold1 fold2 fold3 fold4 fold5)
folder_list2=(fold6 fold7 fold8 fold9 fold10)
folder_list3=(fold11 fold12 fold13 fold14 fold15)
folder_list4=(fold16 fold17 fold18 fold19 fold20)

folder_lists=(folder_list1[@] folder_list2[@] folder_list3[@] folder_list4[@])

for folder_list_selected in "${folder_lists[@]}"; do
    current_list=($(eval echo \${$folder_list_selected}))

    for ((idx = 0; idx < ${#current_list[@]}; idx++)); do
        input_fold=${current_list[idx]}

        echo input_fold $input_fold
        echo result/downstream/${upstream}_${corpus}_$input_fold/dev-best.ckpt

        modelpath=result/downstream/${upstream}_${corpus}_${input_fold}
        if [ -e "${modelpath}/dev-best.ckpt" ]; then
            echo "$modelpath"
        else
            modelpath=${modelpath}_multimodal
            echo "$modelpath"
        fi

        python3 run_downstream.py -m evaluate -e $modelpath/dev-best.ckpt \
                                        -o "config.downstream_expert.datarc.test_fold=${folder_list1[idx]}"
        python3 run_downstream.py -m evaluate -e $modelpath/dev-best.ckpt \
                                        -o "config.downstream_expert.datarc.test_fold=${folder_list2[idx]}"
        python3 run_downstream.py -m evaluate -e $modelpath/dev-best.ckpt \
                                        -o "config.downstream_expert.datarc.test_fold=${folder_list3[idx]}"
        python3 run_downstream.py -m evaluate -e $modelpath/dev-best.ckpt \
                                        -o "config.downstream_expert.datarc.test_fold=${folder_list4[idx]}"
    done
done