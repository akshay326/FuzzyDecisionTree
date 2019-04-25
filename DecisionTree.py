import math


# find item in a list
def find(item, l):
    for i in l:
        if item(i):
            return True
        else:
            return False


# find most common value for an attribute
def majority(attributes, data, target):
    # find target attribute
    val_freq = {}
    # find target in data
    index = attributes.index(target)
    # calculate frequency of values in target attr
    for tuple in data:
        if tuple[index] in val_freq:
            val_freq[tuple[index]] += 1
        else:
            val_freq[tuple[index]] = 1
    max = 0
    major = ""
    for key in val_freq.keys():
        if val_freq[key] > max:
            max = val_freq[key]
            major = key
    return major


# Calculates the entropy of the given data set for the target attr
def entropy(attributes, data, target_attr):
    val_freq = {}
    dataEntropy = 0.0

    # find index of the target attribute
    i = 0
    for entry in attributes:
        if target_attr == entry:
            break
        i += 1

    # Calculate the frequency of each of the values in the target attr
    for entry in data:
        if entry[i] in val_freq:
            val_freq[entry[i]] += 1.0
        else:
            val_freq[entry[i]] = 1.0

    # Calculate the entropy of the data for the target attr
    for freq in val_freq.values():
        dataEntropy += (-freq / len(data)) * math.log(freq / len(data), 2)

    return dataEntropy


def gain(attributes, data, attr, target_attr):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    val_freq = {}
    subset_entropy = 0.0

    # find index of the attribute
    i = attributes.index(attr)

    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if entry[i] in val_freq:
            val_freq[entry[i]] += 1.0
        else:
            val_freq[entry[i]] = 1.0
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
    for val in val_freq.keys():
        valProb = val_freq[val] / sum(val_freq.values())
        dataSubset = [entry for entry in data if entry[i] == val]
        subset_entropy += valProb * entropy(attributes, dataSubset, target_attr)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return entropy(attributes, data, target_attr) - subset_entropy


# choose best attibute
# dont choose target attribute
def choose_attr(data, attributes, target):
    best = attributes[0]
    max_gain = 0
    for attr in attributes:
        if attr != target:
            newGain = gain(attributes, data, attr, target)
            if newGain > max_gain:
                max_gain = newGain
                best = attr
    return best


# get values in the column of the given attribute
def getValues(data, attributes, attr):
    index = attributes.index(attr)
    values = []
    for entry in data:
        if entry[index] not in values:
            values.append(entry[index])
    return values


def get_samples(data, attributes, best, val):
    examples = [[]]
    index = attributes.index(best)
    for entry in data:
        # find entries with the give value
        if entry[index] == val:
            new_entry = []
            # add value if it is not in best column
            for i in range(0, len(entry)):
                if i != index:
                    new_entry.append(entry[i])
            examples.append(new_entry)
    examples.remove([])
    return examples


def make_tree(data, attributes, target, recursion):
    recursion += 1
    # Returns a new decision tree based on the examples given.
    data = data[:]
    vals = [record[attributes.index(target)] for record in data]
    default = majority(attributes, data, target)

    # If the dataset is empty or the attributes list is empty, return the
    # default value. When checking the attributes list for emptiness, we
    # need to subtract 1 to account for the target attribute.
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute to best classify our data
        best = choose_attr(data, attributes, target)
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best: {}}

        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in getValues(data, attributes, best):
            # Create a subtree for the current value under the "best" field
            examples = get_samples(data, attributes, best, val)
            new_attr = attributes[:]
            new_attr.remove(best)
            subtree = make_tree(examples, new_attr, target, recursion)

            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree

    return tree
