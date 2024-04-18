import datetime
import re
from string import Template
t = Template('sum(increase(response_total{cluster="$cluster", namespace="$namespace", direction="outbound"}[1m])) by (status_code)')

# date_time1 = datetime.datetime.fromtimestamp(1713438309)
# date_time2 = datetime.datetime.fromtimestamp(1713438563)
# time1 = date_time1.time()
# time2 = date_time2.time()
# print("time1: ", time1)
# print("time2: ", time2)
# if time2 > time1:
#     print("Yayyyy")


# pattern = r'\$("[^"]+")'
text = 'sum(increase(response_total{cluster="$cluster", namespace="$namespace", direction="outbound"}[1m])) by (status_code)'
# # Find all matches in the text
# matches = re.findall(pattern, text)
# filtered_words = [word[1:] for word in matches]
# print("filtered_words: ", matches)


# variables = []
#
# for ind in range(len(text)):
#     if ind < len(text)-1 and text[ind] == '"' and text[ind+1] == '$':
#         j = ind+2
#         word = ""
#         while text[j] != '"':
#             word = word + text[j]
#             j = j+1
#         variables.append(word)
#         ind = j
#
# print("variables: ", variables)
#
#
def create_query_from_expr(expr, variables):
    t = Template(expr)
    return t.substitute(variables)

    # for var, value in variables.items():
    #     print("var: ", var, "value: ", value)
    #     expr.replace('$'+var, value)
    # return expr

variables = {
    "cluster": "pac-sfcluster01",
    "namespace": "flock"
}
#
# print("query: ", create_query_from_expr(text, variables))
#
#
# tex =
# tex.replace("cluster", "pac-sfcluster01")

print("query: ", create_query_from_expr(text, variables))