
DATA_DIR = "../Data/MSVD/"
MSVD_CSV_DATA_PATH = "../Data/MSVD/MSVD_corpus.csv"
MSVD_PREPROC_CSV_DATA_PATH = "../Data/MSVD/processed_MSVD_corpus.csv"
MSVD_VIDEO_DATA_PATH = "../Data/MSVD/YouTubeClips/"
MSVD_OMMITTED_CAPS_PATH = "../Data/MSVD/MSVD_omitted_caps.txt"
MSVD_FINAL_CORPUS_PATH = "../Data/MSVD/MSVD_final_corpus.csv"

MSVD_VOCAB_PATH = '../Data/MSVD/MSVD_vocab.json'
MSVD_REVERSE_VOCAB_PATH = '../Data/MSVD/MSVD_reverse_vocab.pkl'

MSVD_VID_CAPS_TRAIN_PATH = '../Data/MSVD/MSVD_vid_caps_train.json'
MSVD_VID_CAPS_VAL_PATH = '../Data/MSVD/MSVD_vid_caps_val.json'
MSVD_VID_CAPS_TEST_PATH = '../Data/MSVD/MSVD_vid_caps_test.json'

TOTAL_VIDS = 1970
TRAIN_VIDS = 1200
TEST_VIDS = 670
VAL_VIDS = 100

MSVD_FINAL_CORPUS_TRAIN_PATH = "../Data/MSVD/MSVD_final_corpus_train.csv"
MSVD_FINAL_CORPUS_VAL_PATH = "../Data/MSVD/MSVD_final_corpus_val.csv"
MSVD_FINAL_CORPUS_TEST_PATH = "../Data/MSVD/MSVD_final_corpus_test.csv"

MSVD_VID_IDS_ALL_PATH = "../Data/MSVD/present_vid_ids.txt"

MSVD_VID_IDS_TRAIN_PATH = "../Data/MSVD/vid_ids_train.txt"
MSVD_VID_IDS_VAL_PATH = "../Data/MSVD/vid_ids_val.txt"
MSVD_VID_IDS_TEST_PATH = "../Data/MSVD/vid_ids_test.txt"

MSVD_FRAMES_DIR = "../Data/MSVD/Frames"
MSVD_FEATS_DIR = "../Data/MSVD/Features/"

RESNET_FEAT_DIM = 2048
INCEPTION_FEAT_DIM = 2048
VGG_FEAT_DIM = 512

MAX_FRAMES = 360
FRAME_SPACING = 28

MSVD_DATA_IDS_TRAIN_PATH = "../Data/MSVD/data_ids_train.txt"
MSVD_DATA_IDS_VAL_PATH = "../Data/MSVD/data_ids_val.txt"
MSVD_DATA_IDS_TEST_PATH = "../Data/MSVD/data_ids_test.txt"

SAVE_DIR_PATH = "../Results/Debug/"

params = {
	'dataset_name' : 'MSVD',
    'cnn_name' : 'VGG19',
    'train_data_ids_path' : MSVD_DATA_IDS_TRAIN_PATH,
    'val_data_ids_path' : MSVD_DATA_IDS_VAL_PATH,
    'test_data_ids_path' : MSVD_DATA_IDS_TEST_PATH,
    'vocab_path' : MSVD_VOCAB_PATH,
    'reverse_vocab_path' : MSVD_REVERSE_VOCAB_PATH,
    'mb_size_train' : 1, # 64
    'mb_size_test' : 1, # 128
    'train_caps_path' : MSVD_VID_CAPS_TRAIN_PATH,
    'val_caps_path' : MSVD_VID_CAPS_VAL_PATH,
    'test_caps_path' : MSVD_VID_CAPS_TEST_PATH,
    'feats_dir' : MSVD_FEATS_DIR,
    'save_dir': SAVE_DIR_PATH,
    'word_dim' : 512,	# word embeddings size
    'ctx_dim' : 2048,	# video cnn feature dimension
    'lstm_dim' : 512,	# lstm unit size
    'patience' : 20,
    'max_epochs' : 250,
    'decay_c' : 1e-4,
    'alpha_entropy_r' : 0.,
    'alpha_c' : 0.70602, # 0.70602
    'clip_c': 10.,
    'lrate' : 0.01,
    'vocab_size' : 20000, # n_words
    'maxlen_caption' : 30,	# max length of the descprition
    'optimizer' : 'adadelta',
    'batch_size' : 1, # 64	# for trees use 25
    'metric' : 'everything',	# set to perplexity on DVS # blue, meteor, or both
    'use_dropout' : True,   #True
    'selector' : True, # True
    'ctx2out' : True,  # True
    'prev2out' : True,
    # in the unit of minibatches
    'dispFreq' : 10,    # 10
    'validFreq' : 2000,    # 2000
    'saveFreq' : -1, # this is disabled, now use sampleFreq instead
    'sampleFreq' : 10,   # 100
    'verbose' : True,
    'debug' : False,    # False
    'reload_model' : False, # False
    'from_dir' : '',
    'ctx_frames' : 28, # 26 when compare 
    'random_seed' : 1234,
    'beam_search' : True,
}

'''
Basic LSTM :
    - Only bottom LSTM layer without attention
    - selector : False
    - ctx2out : False
    - prev2out : True
    - alpha_c : 0.
    - alpha_entropy_r : 0.

hLSTMt :
    - 2 layer LSTM with attention but no adjusted attention
    - selector : False
    - ctx2out : True
    - prev2out : True
    - alpha_c : 0.70602
    - alpha_entropy_r : 0.

hLSTMat :
    - 2 layer LSTM with adjusted temporal attention
    - selector : True
    - ctx2out : True
    - prev2out : True
    - alpha_c : 0.70602
    - alpha_entropy_r : 0.
'''
