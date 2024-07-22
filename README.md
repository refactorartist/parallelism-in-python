# Parllelism in Python

This project showcases the various ways to handle IO Bound operations. 

It tries to show a similar simple example for the following:

1. Sequential Programming 
2. Using Multithreading 
3. Using Multiprocessing 
4. Using AsyncIO 

Except for the `Sequential Programming` example, in all cases it simply tries to download 128 urls concurrently. 


## Installing the Project 

After cloning the project, run the following command 

```bash
pdm install 
```

### Listing the Scripts 

Run the following 

```bash
pdm run --list 
```


## Running the Example scripts 

### Sequential Programming Example 

```bash
pdm run sequential
```

### Mutlithreding Example 

```bash
pdm run multithreading
```

### Multiprocessing Example 

```bash
pdm run multiprocessing
```

### AsyncIO 

```bash
pdm run asyncio
```

