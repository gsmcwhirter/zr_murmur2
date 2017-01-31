import murmur2


def _test_murmur2(test_cases):
    for str_, hash32n, hash64a, seed in test_cases:
        assert murmur2.murmur32n(str_, len(str_), seed) == hash32n
        # assert murmur2.murmur64a(str_, len(str_), seed) == hash64a


def test_murmur2():
    tests = [
        ("2e600bad-026a-4258-ba1d-bab4a1517057", 905537245, None, 0),
        ("e0ecd024-3ec4-40f7-a32b-ec2f00eff363", 3607209597, None, 0),
        ("7ad601ce-a502-43be-aa2a-affb64023f98", 3252205157, None, 0),
        ("7eddc716-ef9e-4e79-8cb4-72ee7e436544", 2510473605, None, 0),
        ("3fb3866a-56b6-4583-a553-a6e0d2c99c35", 2304971705, None, 0),
        ("190d52d9-5c2b-4a6d-be2d-8505e36ff8f1", 1030520654, None, 0),
        ("6e99cab1-1572-40e1-a5cb-43f66fe8be25", 1828794305, None, 0),
        ("7564f454-e4ba-49a4-b4c3-dc3dad5a1a84", 2998747286, None, 0),
        ("4d1d9fb7-bc3b-4cc1-a84f-73efd6aa4868", 2000265019, None, 0),
        ("1b5e450c-a5ef-4da1-a922-9ba6bb6be07f", 2830422493, None, 0),
    ]

    _test_murmur2(tests)
