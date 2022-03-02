# Result : Generated 3D nodules
<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/156343946-b1611abf-d825-4aa2-ae3d-ed7b0430c6e2.png"  width="70%" height="70%"/>
</p>


<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/156343951-a1a96a30-6852-4f7a-9a42-acdf657ae9a3.png"  width="70%" height="70%"/>
</p>


<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/156343957-fe349b1f-4e78-4036-9a45-5eb8e9a03263.png"  width="70%" height="70%"/>
</p>


<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/156343964-6d130218-79b2-4f03-baf1-d8a089eb9bc0.png" width="70%" height="70%"/>
</p>


# 3D CT-GAN flow
<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/156343973-9eadbc02-f562-4879-9715-baaf054fae41.png" width="200%" height="200%"/>
</p>

# 1. data preprocessing
    python 1_build_injector_trainset.py
 - you should prepare dicom scans and csv file that has nodule seed.
 - It makes dicom CT scans that has nodules in to a numpy array only has nodule bbox(generate 'unhealthy_samples.npy')

 # 2. train
    python 2_train_injector.py

 # 3. test generation model
    python 3_inject_evidence.py
 - Prepare CT scan and designate the seed that you want to insert GAN-fake nodule.


