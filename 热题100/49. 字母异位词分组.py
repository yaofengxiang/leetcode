# 给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
#
# 示例1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# 解释：
# 在strs中没有字符串可以通过重新排列来形成"bat"。字符串"nat"和"tan"是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串"ate" ，"eat"和"tea"是字母异位词，因为它们可以重新排列以形成彼此。
#
# 示例2:
# 输入: strs = [""]
# 输出: [[""]]
#
# 示例3:
# 输入: strs = ["a"]
# 输出: [["a"]]

# 思路：遍历数组，将当前字符串中字母按照字母表排序，检查是否存在于哈希表当中，如果存在，就是“字母异位词”，如果不存在，建立新的表项。
# 以排序过的字符串作为键，以字符串的索引作为字典的值。
def groupAnagrams(strs):
    hashtable = dict()
    for i, cur_str in enumerate(strs):
        # 将cur_str按照字母表进行排序
        char_list = list(cur_str)
        char_list.sort()
        sorted_str = ''.join(char_list)
        if sorted_str in hashtable:  # 表示哈希表中已经存在
            hashtable[sorted_str].append(i)
        else:
            hashtable[sorted_str] = [i]  # 在哈希表中创建某种字母异位词的第一个索引

    # 将哈希表中的内容返回
    ret = list()
    for values in hashtable.values():
        tmp = list()
        for i in values:
            tmp.append(strs[i])
        ret.append(tmp)
    return ret
