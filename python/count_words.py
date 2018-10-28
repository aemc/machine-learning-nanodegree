from collections import Counter

def count_words(s, n):
    return Counter(s.split()).most_common(n)

def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))

if __name__ == '__main__':
    test_run()