# K-means-Clustering

* Task
  1. K-means Algorithm을 MapReduce에 사용하여 K= 10인 각 cluster의 centroid vector 찾기
     
  2. Initial centroid를 4가지로 랜덤하게 구한 후 가장 적합한 initial centroid 찾기
     
  3. (2)에서 구한 initial centroid를 사용하여 test set에 적용한 후 accuracy 확인하기
     
</br>

* Implementation
  
  a. Run mapper, reducer file
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
