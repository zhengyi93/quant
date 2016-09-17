# Data Extraction [Inference Module]
# Currently supports a few instances of quandl imports
# Attempts to infer call to closest match (Edit Distance)
import quandl
import distance

# Assign appropriate keys to required data from Quandl
# TODO: Add regex interpreter
Collection = {
    "US Rates": "FED/SVENY",
    "USD/SGD FX": "FED/RXI_N_A_SI",
}


def extract(inquiry):
    return quandl.get(Collection[correction(inquiry)])


def correction(inquiry):
    m = 9999.0
    sol = ""
    for key in Collection.keys():
        d = distance.nlevenshtein(inquiry, key)
        if d < m:
            m = d
            sol = key
    return sol
