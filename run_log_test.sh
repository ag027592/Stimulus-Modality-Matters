# bash run_multilabel_test.sh
# for upstream in apc_960hr; do
for upstream in wavlm_large wav2vec2_large_lv60_cv_swbd_fsh xls_r_1b data2vec_large_ll60k hubert_large_ll60k wav2vec2_large_960 vq_wav2vec wav2vec_large decoar2 tera_960hr mockingjay_960hr npc_960hr vq_apc_960hr apc_960hr; do
    echo $upstream
    bash run_multimodal_result.sh 1 ${upstream} > logs/${upstream}_fold1.txt

    echo fold1 > logs/${upstream}_log.txt
    python test_multimodal.py --input_file logs/${upstream}_fold1.txt >> logs/${upstream}_log.txt
done