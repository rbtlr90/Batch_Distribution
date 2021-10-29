# Batch Distributer
Algorithm trial for distributing batches to each servers equally - Pseudo code version.
GOAL: Minimize difference between the greatest and the smallest batch bundle with acceptable time/space complexity.


## Description for the process
1. Sort the samples. Python already has a great sorting algorithm(Timsort which combined with insertion and merge sort), so I don't need to implement sorting algorithm.
2. Implement AVL tree that consisted with some Nodes that contains both key and value.
3. Distribute the batches due to algorithm
4. Run command
    ```bash
    python3 batch_distribution.py --N 1000 --M 20
    ```

## Results
1. In case of N = 2000, M = 100, randrange(100, 10000)
    ```bash
    max average: 100699
    min average: 100566
    max - min average : 133
    diff / min average : 0.00132
    execution time average: 0.023
    ```
2. In case of N = 2000, M = 100, randrange(1, 10000)
    ```bash
    max average: 99512
    min average: 99380
    max - min average : 132
    diff / min average : 0.00132
    execution time average: 0.023
    ```
3. In case of N = 1000, M = 100, randrange(100, 10000)
    ```bash
    max average: 49833
    min average: 49668
    max - min average : 165
    diff / min average : 0.0033
    execution time average: 0.011
    ```
4. In case of N = 1000, M = 100, randrange(1, 10000)
    ```bash
    max average: 50499
    min average: 50243
    max - min average : 256
    diff / min average : 0.0050
    execution time average: 0.011
    ```
