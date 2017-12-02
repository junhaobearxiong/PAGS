
<<<<<<< HEAD
def hash_function(item):
    h = hash(item)
    return int(1 << (h%64)) | int(1 << (h//64%64))

def mask(val):
    return bin(hash_function(val))[2:]
=======
def hashfn(item):
    h = hash(item)
    return (1 << (h%64)) | (1 << (h/64%64))

def mask(val):
    return bin(hashfn(val))[2:]
>>>>>>> 5f4cea53435f320a39a8b64b2f62b560e22468fe

class CountingBloom(object):
    def __init__(self):
        self.items = [0] * 64
    def add(self, item):
        bits = mask(item)
        for index, bit in enumerate(bits):
            if bit == '1':
                self.items[index] += 1
    def query(self, item):
        bits = mask(item)
        for index, bit in enumerate(bits):
            if bit == '1' and self.items[index] == 0:
                return False
        return True
    def remove(self, item):
        bits = mask(item)
        for index, bit in enumerate(bits):
            if bit == '1' and self.items[index]:
                self.items[index] -= 1

<<<<<<< HEAD
def remove_singletons(counting_bloom):


=======
>>>>>>> 5f4cea53435f320a39a8b64b2f62b560e22468fe
bloom = CountingBloom()
args = ('foo', 'bar', 'baz')
for arg in args:
    bloom.add(arg)
<<<<<<< HEAD
print(', '.join(str(bloom.query(arg)) for arg in args))
=======
    print(', '.join(str(bloom.query(arg)) for arg in args))
>>>>>>> 5f4cea53435f320a39a8b64b2f62b560e22468fe
for arg in args:
    bloom.remove(arg)
print(', '.join(str(bloom.query(arg)) for arg in args))