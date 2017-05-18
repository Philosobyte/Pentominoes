load pentomino_train_all

rng(2);
len = length(samples);
cutoff = int64(len*0.70);
indices = randperm(len);
trainsamples = samples(:, :, 1, indices(1:cutoff));
traintargets = targets(indices(1:cutoff));
testsamples = samples(:, :, 1, indices(cutoff + 1:len));
testtargets = targets(indices(cutoff + 1:len));

layers = [imageInputLayer([8 8 1]);
          convolution2dLayer(5, 25, 'Padding', [5 5]);
          reluLayer();
          maxPooling2dLayer(5,'Stride', 5);
          fullyConnectedLayer(18);
          softmaxLayer();
          classificationLayer()];  
      
options = trainingOptions('sgdm', 'MaxEpochs', 200, 'L2Regularization', 0.0005, 'InitialLearnRate', 0.04);  
net = trainNetwork(trainsamples,traintargets,layers,options);  
actualtargets = classify(net,testsamples);
[testtargets(1:10, :) actualtargets(1:10, :)]
accuracy = sum(actualtargets == testtargets)/numel(testtargets)