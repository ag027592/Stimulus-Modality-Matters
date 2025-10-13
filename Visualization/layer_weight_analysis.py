# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:36:46 2024

@author: Huang-Cheng Chou
"""
import pandas as pd
import glob
import numpy as np
from sklearn.metrics import classification_report
import torch
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

plt.rcParams["figure.figsize"] = (40,10)
plt.rcParams.update({'font.size': 60})


# fold1~fold5: voice-only
# fold6~fold10: audio-visual
# fold11~fold15: combine all
# fold16~fold20: face-only

weights_dict = {
    "Voice":[],
    "Face":[],
    "AV":[],
    "All":[]
        }

files = glob.glob('./WavLM/*/dev-best.ckpt')

m = torch.nn.Softmax(dim=0)


for each_file in files:
    infro_list = each_file.split("\\")
    train_set = int(infro_list[1].split("_")[3].replace("fold",""))
 
    if train_set in [1,2,3,4,5]:
        train = "Voice"
    elif train_set in [6,7,8,9,10]:
        train = "AV"
    elif train_set in [11,12,13,14,15]:
        train = "All"
    elif train_set in [16,17,18,19,20]:
        train = "Face"
    
    # raw_infor = torch.load(each_file)
    weights = m(torch.load(each_file)['Featurizer']['weights']).cpu().numpy().reshape(1,-1)
    
    
    weights_dict[train].append(weights)
    
averaged_weights_dict = {
    "Voice":[],
    "Face":[],
    "AV":[],
    "All":[]
        }

for modaly in weights_dict:
    
    cur_data = np.mean(np.vstack(weights_dict[modaly]),0)
    
    averaged_weights_dict[modaly] = cur_data
    

# Within models, across databases
       
markers = ['o', 'x', '+', '^'] #, 'v', 's', 'D', '*', 'p']        
colors = ['red', 'blue', 'green', 'orange'] #, 'purple', 'cyan', 'magenta', 'lime']


for index, model_name in enumerate(list(averaged_weights_dict.keys())):
    
    if model_name != "All":
        cur_avg_np = averaged_weights_dict[model_name]
        
        x_index = np.arange(1,26)
        
        plt.xticks(x_index)
        
        #plt.xlim(0.5,cur_np.shape[1]+0.5)
        
        plt.plot(x_index,cur_avg_np,marker=markers[index % len(markers)],linestyle='--', linewidth=4, markersize=20,label=model_name, color=colors[index % len(colors)]) 
        
        plt.grid(True)
        plt.xlabel("Layer")
        plt.ylabel("Weights")
        # plt.title(model_name)
        save_path = 'across_modality.pdf'
        l4 = plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=4)
plt.savefig(save_path,format="pdf", bbox_inches='tight',dpi=800)
plt.show()




