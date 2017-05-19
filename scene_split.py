pr_feature=[]
feature=np.random.normal(size=[15,14,16])

num_frames=np.array([8,5,6,8,5,6,8,5,6,8,5,6,8,5,6])
for i in range(feature.shape[0]):
    numvec = (feature[i][1:num_frames[i]] *feature[i][0:num_frames[i]-1]).sum(axis=1)/(np.sqrt((feature[i][1:num_frames[i]]**2).sum(1))*(np.sqrt((feature[i][0:num_frames[i]-1]**2).sum(1))))
    np.sort(numvec)
    scene = (numvec<0.25)
    scene[0]
    idx = np.where(scene)[0]+1
    example_splits = np.split(feature[i][:num_frames[i]], idx,0)
    
    example_splits_mean = [np.mean(example_split,0) for example_split in example_splits ]
    example_splits_mean = np.stack(example_splits_mean, 0)
    example_splits_mean

    sh = list(example_splits_mean.shape)
    sh[0] = 14 - sh[0]
    example_splits_mean = np.concatenate([example_splits_mean, np.zeros(sh)], 0)

    pr_feature.append(example_splits_mean)
pr_feature=np.stack(pr_feature, 0)
pr_feature.shape
