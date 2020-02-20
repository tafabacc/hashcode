import math

filename = "c_incunabula"
with open(f'./{filename}.txt', 'r') as file:
    data = file.read()

data = data.split('\n')
# B books, L libraries, D days
B, L, D= [int(row) for row in data[0].split(' ')]

# S: Score by book b
S = [int(row) for row in data[1].split(' ')]

l_sections = data[2:]

libraries = []

def get_score(books):
    scores = 0
    for b in books:
        scores += S[b]
    # total_score
    return scores

# score max dans le min de temps
# taken: T, M
# scanning_time = math.ceil(N / M)
# total_time = T + scanning_time
# scores
# calcul rate score / time

#  hevitra 1: isan'ny boky kely fa score lehibe
def total_score(lib):
    books = lib["books"]
    return get_score(books)

# L sections
for section_id in range(L):
    line_1 = l_sections[section_id *2]
    line_2 = l_sections[section_id *2 +1]

    # N: Number of books in the library
    # T: Time for signup process
    # M: number of books that can be scanned by day
    N, T, M = [int(row) for row in line_1.split(' ')]
    books = [int(row) for row in line_2.split(' ')]
    time = math.ceil(N / M)

    library = { "id": section_id, "N": N, "T": T, "M": M, "books": books,
            "score": get_score(books), "time": time}

    libraries.append(library)

# weigth (>)
# greater M
# lower T
# lower N
# greater scores

# compute books_score, order books_score
#sorted_libraries = reversed(sorted(libraries, key=total_score))
sorted_libraries = reversed(sorted(libraries,
    key=lambda l: ((l["score"] / l["T"]) * l["M"] / l["N"]) / l["time"]))


# the hard thing starts here
printed_streams = []

# to file
def tof(line):
    printed_streams.append(line)

tof(f"{len(libraries)}")

#for i,scanned_lib in enumerate(libraries):
for i,scanned_lib in enumerate(sorted_libraries):

    tof(f'{str(str(scanned_lib["id"]))} {str(scanned_lib["N"])}')

    books =" ".join([str(b) for b in scanned_lib["books"]])
    tof(books)


with open(f"./{filename}.txt.out", "w") as file:
    for line in printed_streams:
        file.write(f"{line}\n")

print("Done")



# numer of all books, ID 0 to B-1
B = 0
books = [] # length B

# book
# - score

# librairies
L = 0
# library
# - books: set of books in the library
# - time: (days) time to sign up
# - nbpd: nb of books that can be scanned each day

# time: total time
D = 0

# signup:
# - only one library at a time

# book scan:
# - once the library is scanned
# - parallel scanning from multiple libraries from multiple libraries

