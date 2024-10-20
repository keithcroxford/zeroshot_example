# Background

Experimenting with ML models isn't limited to only those with a deep understanding of ML algorithms. If you have a little bit of Python knowledge, you can experiment with TONS of different models that are available on Hugging Face (https://huggingface.co/tasks/zero-shot-classification)!

# What is Zero Shot Classification

According to Hugging Face "Zero-shot text classification is a task in natural language processing where a model is trained on a set of labeled examples but is then able to classify new examples from previously unseen classes." 

Personally, I see this akin to teaching a child the differnce between dogs, cats, birds, and fish. Eventually the child will see a new animal that matches one of those types (such as a tiger), and will assume that it is a cat even though they've never seen a tiger. 

# Dependencies 
- You need Python >= 3.11
- Pandas, and the transformers libs must be installed on you machine.

#How  to run 
- Clone the repo
- Ensure that dependencies are handled
- run `python example.py`. This will process a very simple CSV that ChatGPT generated.
  - If you have your own CSV to process ensure that it is has  "Description" and "Category" fields.
  - Update the candidate labels to reflect your own use case.

# Example Results
```
Ticket #: 1 | Known Category: BGP Routing | Zero Shot Category: Routing | Zero Shot Probability: 0.8544367551803589
Ticket #: 2 | Known Category: Password Reset | Zero Shot Category: Password Resets | Zero Shot Probability: 0.7400564551353455
Ticket #: 3 | Known Category: Spam | Zero Shot Category: Spam | Zero Shot Probability: 0.8751707673072815
Ticket #: 4 | Known Category: Web Portal Issues | Zero Shot Category: Web Portal Issues | Zero Shot Probability: 0.9409095644950867
Ticket #: 5 | Known Category: Maintenance Notice | Zero Shot Category: Maintenance Notices | Zero Shot Probability: 0.6111332178115845
Ticket #: 6 | Known Category: BGP Routing | Zero Shot Category: Routing | Zero Shot Probability: 0.9103394746780396
Ticket #: 7 | Known Category: Password Reset | Zero Shot Category: Web Portal Issues | Zero Shot Probability: 0.4031056761741638
Ticket #: 8 | Known Category: Spam | Zero Shot Category: Spam | Zero Shot Probability: 0.9286561012268066
Ticket #: 9 | Known Category: Web Portal Issues | Zero Shot Category: Web Portal Issues | Zero Shot Probability: 0.8927190899848938
Ticket #: 10 | Known Category: Maintenance Notice | Zero Shot Category: Maintenance Notices | Zero Shot Probability: 0.5159217119216919
```
