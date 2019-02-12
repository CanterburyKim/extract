# TODO: write your function defs here








# TEST CASES BEGIN HERE

class TestExtract(unittest.TestCase):
    """
    test class
    """

    first_list = [ 'hello.txt', 'goodbye.txt', 'smooth.mp3', 'nice.mp4', 'saucy.aac']
    second_list = ['xx.mkv', 'mr2.jpg', 'go_away.gif', 'vhat.png', 'slik.mp3']

    def test_extract_A(self):

        extract_A(first_list, second_list)

    # TODO: add other test cases needed to test the functions



if __name__ == '__main__':
    unittest.main()
