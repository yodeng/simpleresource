# Simple Resource Limite Decorators For Python Runtime

## Decorators:

### @set_runtime(seconds=0)

```
RuntimeError, max runtime of the function in decorators
```



### @set_cpu_runtime(seconds=0)

```
RuntimeError, max soft cpu runtime of the function in decorators
```



### @set_max_memory(size=0)

```
max memory of the function in decorators
```



### @set_max_cpu(nproc=65535)

```
max ncpu of the function in decorators
```



### set_max_cpu0(nproc=65535)

```
max ncpu of the function in main process, can not be used for decorators
```

## Usage:

```python
@set_runtime(seconds=5)
def test():
	time.sleep(10)
test()
## RuntimeError
	
```

## Install

```
pip install simpleresource

or:

pip install git+https://github.com/yodeng/simpleresource.git
```



