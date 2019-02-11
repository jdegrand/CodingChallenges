# You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times you showed an ad on each individual domain. Every line consists of a count and a domain name. It looks like this:
from collections import defaultdict

counts = ["900,google.com",
          "60,mail.yahoo.com",
          "10,mobile.sports.yahoo.com",
          "40,sports.yahoo.com",
          "300,yahoo.com",
          "10,stackoverflow.com",
          "2,en.wikipedia.org",
          "1,es.wikipedia.org",
          "1,mobile.sports"]


# Write a function that takes this input as a parameter and returns a data structure containing the number of hits that were recorded on each domain AND each domain under it. For example, an impression on "mail.yahoo.com" counts for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains. Note that "mobile.sports" appears as a separate domain as the last item of the input.)

# Sample output (in any order/format):

# getTotalsByDomain(counts)
# 1320    com
#  900    google.com
#  410    yahoo.com
#   60    mail.yahoo.com
#   10    mobile.sports.yahoo.com
#   50    sports.yahoo.com
#   10    stackoverflow.com
#    3    org
#    3    wikipedia.org
#    2    en.wikipedia.org
#    1    es.wikipedia.org
#    1    mobile.sports
#    1    sports

def getTotalsByDomain(counts):
    dic = defaultdict(int)
    # "60,mail.yahoo.com",
    for element in counts:
        element = element.strip().split(",")
        domains = element[1].split(".")
        dic[domains[-1]] += int(element[0])
        while len(domains) > 1:
            end = domains.pop()
            front = domains.pop()
            s = front + "." + end
            dic[s] += int(element[0])
            domains.append(s)
    for k, v in dic.items():
        print(k + ":", v)

def main():
    getTotalsByDomain(counts)

if __name__ == '__main__':
    main()
