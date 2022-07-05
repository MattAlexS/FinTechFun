import yfinance as yf


msft = yf.Ticker("msft").history(period="max")
msft['msft'] = msft['Close'] - msft['Open']
msft[msft['msft'] <= 0.5] = int(0)
msft[msft['msft'] > 0.5] = int(1)
msft.loc[(msft.msft == 0),'msft']= '-'
msft.loc[(msft.msft == 1),'msft']= '+'



def recurse(alphabet, length):
    out = []
    for i in range(length):
        if len(out) == 0:
            for letter in alphabet:
                out.append(letter)
        else:
            new = []
            for pre in out:
                for letter in alphabet:
                    new.append(pre+letter)
            out = new
    return out
        

def hmm(alphabet,window, data):
    probs = {}
    pos = recurse(alphabet, window)
    for i in pos:
        probs[i] = [0,0]
    
    for i in range(len(data)-(window)):
        prior = []
        for x in range(window):
            prior.append(data.iloc[i+x])
        prior = ''.join(prior)
        post = data.iloc[i+window]
        probs[prior][1] += 1
        if post == '+':
            probs[prior][0] += 1
    return probs

    
