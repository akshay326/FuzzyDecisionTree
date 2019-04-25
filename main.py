import DecisionTree
import DrawTree
from sklearn.model_selection import train_test_split


# test data without attributes
# returns misses and errors
def test(test_data, attributes, tree, target_attribute):
    count, miss, err = 0, 0, 0
    x = attributes.index(target_attribute)

    for entry in test_data:
        count += 1
        temp_dict = tree.copy()
        result = ""
        while isinstance(temp_dict, dict):
            fk = next(iter(temp_dict))  # first key
            temp_dict = temp_dict[fk]
            index = attributes.index(fk)
            value = entry[index]
            if value in temp_dict.keys():
                result = temp_dict[value]
                temp_dict = temp_dict[value]
            else:
                miss += 1
                result = "?"
                break

        # check if correct
        if result != entry[x]:
            err += 1
        print("entry%s = %s" % (count, result))

    return count, miss, err


def read_csv(data_file, parse_attributes=False):
    # read raw data
    data = [[]]
    with open(data_file) as f:
        for line in f:
            line = line.strip("\r\n")
            data.append(line.split(','))
    data.remove([])

    if parse_attributes:
        attributes = data[0]
        data.pop(0)  # remove attributes from it
        return data, attributes
    else:
        return data


# assuming obj is a dict. count it as a valid node
# returns non terminal, terminal nodes in that tree
def info(obj, depth=0):
    ntn, tn = 0, 0
    for k, v in obj.items():
        if isinstance(v, dict):  # if valid subtree
            ntn1, tn1 = info(v, depth=depth + 1)
            tn += tn1
            ntn += ntn1

            if depth % 2 == 0:
                ntn += 1
        else:  # not a subtree -> means a leaf
            tn += 1
    return ntn, tn


def main():
    # # single data file
    file_name, target_attribute = 'datasets/bool_or.csv', 'output'
    data, attributes = read_csv(file_name, parse_attributes=True)
    train_data, test_data = train_test_split(data, test_size=0.3, shuffle=True)  # split in train and test data

    # separate data files
    # train_file, test_file, target_attribute = 'datasets/VoteTraining.csv', 'datasets/Vote.csv', 'class'
    # train_file, test_file, target_attribute = 'datasets/WeatherTraining.csv', 'datasets/Weather.csv', 'play'
    # train_file, test_file, target_attribute = 'datasets/SoybeanTraining.csv', 'datasets/Soybean.csv', 'class'
    # train_data, attributes = read_csv(train_file, parse_attributes=True)
    # test_data = read_csv(test_file)

    print("%d training sample, %d testing samples" % (len(train_data), len(test_data)))

    # don't know where it comes from
    while [''] in train_data:
        train_data.remove([''])
    while [''] in test_data:
        test_data.remove([''])

    # Run ID3 to generate a tree
    m_tree = DecisionTree.make_tree(train_data, attributes, target_attribute, 0)

    a, b = info(m_tree)
    print("Decision Tree contains %d judging attributes" % a)
    DrawTree.DrawTree(m_tree)

    # tree and list of attributes
    count, miss, err = test(test_data=test_data, tree=m_tree, attributes=attributes, target_attribute=target_attribute)

    print("%d total test cases, %d missed, %d wrong" % (count, miss, err))


if __name__ == '__main__':
    main()
