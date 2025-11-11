"""
HW05 — City Bike Registry (Resizing Chaining Map)
"""
class HashMap:
    """Chaining hash map with auto-resize at load factor > 0.75."""

    def __init__(self, m=4):
        # TODO: create m empty buckets and set size counter
        self.buckets = [[] for _ in range(m)]
        self.count = 0

    def _hash(self, s):
        """Return simple integer hash for string s."""
        # TODO: sum character ordinals or similar
        return sum(ord(c) for c in s)

    def _index(self, key, m=None):
        """Return bucket index for key with current or given bucket count."""
        # TODO
        if m is None:
            m = len(self.buckets)
        return self._hash(key) % m

    def __len__(self):
        """Return number of stored pairs."""
        # TODO
        return self.count

    def _resize(self, new_m):
        """Resize to new_m buckets and rehash all pairs."""
        # TODO: allocate new buckets; reinsert all pairs
        old_pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                old_pairs.append((k, v))
        self.buckets = [[] for _ in range(new_m)]
        self.count = 0
        for k, v in old_pairs:
            self.put(k, v)

    def put(self, key, value):
        """Insert or overwrite. Resize first if load will exceed 0.75."""
        # TODO: check load; maybe resize; then insert/overwrite
        if (self.count + 1) / len(self.buckets) > 0.75:
            self._resize(len(self.buckets) * 2)
        i = self._index(key)
        bucket = self.buckets[i]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        """Return value for key or None if missing."""
        # TODO
        i = self._index(key)
        for k, v in self.buckets[i]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove key if present. Return True if removed else False."""
        # TODO
        i = self._index(key)
        bucket = self.buckets[i]
        for j, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(j)
                self.count -= 1
                return True
        return False

if __name__ == "__main__":
    # Optional manual check
    pass
