# K-means-Clustering


* Goal

  
  MNIST dataset (60000 training data, 10000 test data)을 이용하여 K-mean algorithm 구현하고 적합한 initial centroid 를 찾어 test set에 적용하여 정확도 확인하기

  
* Task
  
  1. K-means Algorithm을 MapReduce에 사용하여 K= 10인 각 cluster의 centroid vector 찾기
     
  2. Initial centroid를 4가지로 랜덤하게 구한 후 가장 적합한 initial centroid 찾기
     
  3. (2)에서 구한 initial centroid를 사용하여 test set에 적용한 후 accuracy 확인하기
     
</br>

* Implementation
  
  a. Run mapper, reducer file

  i) K-means Algorithm을 MapReduce에 사용하여 K= 10인 각 cluster의 centroid vector 찾기
  - 첫번째 MapReduce job : initial centroid를 기준으로 각 img의 minimum distance를 종합해 새로운 centroids 구하기
  
   ```sh
   for i in `seq 1 10`:
   do
     hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D mapred.job.name='job' \
    -D mapred.map.tasks = 20 \
  	-D mapred.reduce.tasks = 10 \
  	-file ./hw3/mapper1.py -mapper mapper1.py \
    -file ./hw3/reducer1.py -reducer reducer1.py \
  	-input ./hw3/train_img \
  	-output ./hw3/output1

    hdfs dfs -cat ./hw3/output1/* > ./hw3/new_cent
    cat ./hw3/new_cent > ./hw3/new_cent1.txt
    cat ./hw3/new_cent1.txt > ./res.txt
    hdfs dfs -rm -r ./hw3/output1
   done
   ```
   
  b. Move input file
  ```sh
  hdfs dfs -copyFromLocal hw3/train_img ./hw3
  ```

  c. check output file
  ```sh
  hdfs dfs -cat hw3/output1/part-00000 | head -10
  ```

  d. Remove output file
  ```sh
  hdfs dfs -rm -r ./hw3/output1
  ```

* Result
  1. K= 10인 각 cluster의 centroid vector 찾기 (왼쪽 : Centroid 번호, digit 이미지의 숫자)
 
     
     ![image](https://github.com/guswns00123/K-means-Clustering/assets/65805176/91e1bb8c-a146-4082-85a7-879016b147c3)



  2. Initial centroid를 4가지로 랜덤하게 구한 후 가장 적합한 initial centroid 찾기
     1) Random Seed 1000으로 구한 Centroid
     ![image](https://github.com/guswns00123/K-means-Clustering/assets/65805176/b6486e2e-c68e-43e4-a826-34d5f93bbef9)


     2) Random Seed 2000으로 구한 Centroid
     ![image](https://github.com/guswns00123/K-means-Clustering/assets/65805176/98229e9b-17c2-4493-a7dc-5694e824e295)


     3) 주어진 Seed로 구한 Centroid
     ![image](https://github.com/guswns00123/K-means-Clustering/assets/65805176/5945cefa-384b-4d8b-bafd-3c2e725a5d33)



  3. (2)에서 구한 initial centroid를 사용하여 test set에 적용한 후 accuracy 확인하기
     ![image](https://github.com/guswns00123/K-means-Clustering/assets/65805176/012e52a2-8781-4f04-a0b8-169b81fff1f7)





