#!/usr/bin/env python

import sys

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.transforms as mtransforms

# analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix
# analysis/hic_results/matrix/ddCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix
# analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed

def get_bins(bin_fname, chrom, start, end):    
    frags = np.loadtxt(bin_fname, dtype=np.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    start_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    return start_bin, end_bin
    
def process_data(fname, start, end):
    data = np.loadtxt(fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data = data[np.where((data['F1'] >= start) & (data['F2'] < end))]
    data['score'] = np.log(data['score']) 
    data['score'] = data['score'] - np.min(data['score'])

    adjust = data['F1'][0]

    data['F1'] = data['F1'] - adjust
    data['F2'] = data['F2'] - adjust
    return data 

def populate_matrix(data, dim):
    mat = np.zeros((dim, dim))

    mat[data['F1'], data['F2']] = data['score']
    mat[data['F2'], data['F1']] = data['score']
    return mat

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = np.copy(mat)
    for i in range(N):
        bg = np.mean(mat[np.arange(i, N), np.arange(N - i)])
        mat2[np.arange(i, N), np.arange(N - i)] -= bg
        if i > 0:
            mat2[np.arange(N - i), np.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = np.where(mat[1:-1, 1:-1] == 0)
    nmat = np.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat


if __name__ == "__main__":
    dd_matrix = 'analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix'
    d_matrix = 'analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix'
    bin_fname = 'analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed'

    start, end = get_bins(bin_fname, b'chr15', 11170245, 12070245)

    dim = end - start
    dd_data = process_data(dd_matrix, start, end)
    d_data = process_data(d_matrix, start, end)

    dd_mat = populate_matrix(dd_data, dim)
    d_mat = populate_matrix(d_data, dim)

    fig, axs = plt.subplots(1,3)

    vmax = np.max([np.max(dd_mat), np.max(d_mat)])

    axs[0].imshow(-1*dd_mat, cmap='magma', vmin=-vmax, vmax=0)
    axs[1].imshow(-1*d_mat, cmap='magma', vmin=-vmax, vmax=0)
    axs[2].imshow((smooth_matrix(remove_dd_bg(d_mat))-smooth_matrix(remove_dd_bg(dd_mat))), cmap='seismic', norm=colors.CenteredNorm())
    
    axs[0].axis('off')
    axs[1].axis('off')
    axs[2].axis('off')

    axs[0].set_title('ddCTCF')
    axs[1].set_title('dCTCF')
    axs[2].set_title('dCTCF - ddCTCF')

    plt.suptitle('HiC plot for chr15:11170245-12070245')
    plt.tight_layout()
    plt.savefig('hiC.png')

    ### FULL DATA SETS ### Still looking at chr15:11170245-12070245
    dd_full = 'matrix/ddCTCF_full.6400.matrix'
    d_full = 'matrix/dCTCF_full.6400.matrix'

    start, end = get_bins('matrix/6400_bins.bed', b'chr15', 11170245, 12070245)
    dd_all = process_data(dd_full, start, end) 
    d_all = process_data(d_full, start, end) 
    
    dim = end - start
    
    d_mat = populate_matrix(d_all, dim)
    dd_mat = populate_matrix(dd_all, dim)
    
    fig, axs = plt.subplots(1,3)

    vmax = np.max([np.max(dd_mat), np.max(d_mat)])

    axs[0].imshow(-1*dd_mat, cmap='magma', vmin=-vmax, vmax=0)
    axs[1].imshow(-1*d_mat, cmap='magma', vmin=-vmax, vmax=0)
    axs[2].imshow((smooth_matrix(remove_dd_bg(d_mat))-smooth_matrix(remove_dd_bg(dd_mat))), cmap='seismic', norm=colors.CenteredNorm())
    axs[0].set_title('ddCTCF')
    axs[1].set_title('dCTCF')
    axs[2].set_title('dCTCF - ddCTCF')

    axs[0].axis('off')
    axs[1].axis('off')
    axs[2].axis('off')

    plt.suptitle('HiC plot for full 6400 data set, chr15:11170245-12070245')
    plt.tight_layout()
    plt.savefig('hiC_full.png')

    ### INSULATION SCORES ###
    # Now insulation scores for 10400000-13400000
    d_full = 'matrix/dCTCF_full.40000.matrix'

    # start, end = get_bins('matrix/40000_bins.bed', b'chr15', 10400000, 13400000)
    # print(start,end) # Note, the end I find is 54954 which is not what the HW listed (54951)
    start = 54878
    end = 54951
    d_all = process_data(d_full, start, end) 

    dim = end - start

    d_mat = populate_matrix(d_all, dim)
    d_insul = []

    for i in range(d_mat.shape[0]):
        d_insul.append(np.mean(d_mat[(i - 5):i, i:(i + 5)]))

    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    im = ax[0].imshow(-1*d_mat, cmap='magma', vmin=-np.max(d_mat), vmax=0)

    # Rotate so that diagonal is on the x axis
    trans_data = mtransforms.Affine2D().rotate_deg(-45).translate(0,19) + ax[0].transData
    im.set_transform(trans_data)
    ax[0].set_xlim(-1, 103)
    ax[0].set_ylim(19, 75)

    ax[1].plot(np.arange(len(d_insul)), d_insul)
    plt.margins(x=0)
    ax[1].set_xticks([0, len(d_insul)-1])
    ax[1].set_xticklabels([10400000, 13400000])

    ax[1].set_ylabel('Insulation score')

    ax[1].set_xlabel('Position')

    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0)
    plt.suptitle('HiC and insulation scores')
    plt.tight_layout()
    plt.savefig('hic_insulation.png')


    
    

