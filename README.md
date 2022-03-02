# 1. data preprocessing
    python 1_build_injector_trainset.py
 - you should prepare dicom scans and csv file that has nodule seed.
 - It makes dicom CT scans that has nodules in to a numpy array only has nodule bbox(generate 'unhealthy_samples.npy')

 # 2. train
    python 2_train_injector.py

 # 3. test generation model
    python 3_inject_evidence.py
 - Prepare CT scan and designate the seed that you want to insert GAN-fake nodule.


