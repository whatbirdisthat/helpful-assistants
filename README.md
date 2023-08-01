# Helpful Assistants
A UI using the new Gradio [**ChatInterface**](https://gradio.app/docs/chatinterface) and ChatGPT.

This UI keeps a log of interactions with OpenAI in a very simple text format that
might be useful in the future.

In case you read the README, running `Make run` will result in an error the first time
because the folder `chat-logs` is missing.

## Setup

```shell
mkdir chat-logs
```

**TODO**:
* LHS Sidebar with "Characters"
* Each character is some kind of "expert"
* Each expert provides the system prompt i.e. "You are a scientist" or "You are a literary expert"
* **Behave**, **Playwright**, **unittest** for outside-in testing

This is an experiment to see how alterations to system prompt change the way ChatGPT responses to questions differ
based on the system prompt.

## Setup with Conda

I set up a new environment to build gradio-openai projects called "gru".
There's no need to pin at python 3.10 for transformers or whatnot, since
the model we're using is on the internet, behind an API.

### A Note About Conda

I'm using Conda for the 1.5th time, and I'm not certain that:
1. I know what I'm doing
2. I need to actually use it
3. It's fine
4. I should just use `venv`

One thing I want to note is that if I did not specify the python version
in the `conda create` command the environment was messy, and I got errors
about missing libraries etc, even though I was using `conda install`. I 
found that by using `conda create` and `pip install` I was able to get a
stable environment and no flaky weirdness about missing libraries or missing
constants.

Once you start using Conda, it's best to keep using Conda. But conda install 
doesn't get you the libraries you want: so you use pip to get the libraries...

So why use Conda at all? Why not just use `python -m venv` ...? I'm starting to 
think that way myself.

```shell
conda create --name gru python=3.11 # you don't need to do this
pip install -r requirements.txt
```

It's all a bit confusing, but I **think** all the things I'm installing using `pip`
are being isolated into the `gru` environment but who knows it's all "magic".

Another thing I'll note is that I have two copies of this on my system, both using 
the `gru` Conda environment, and I think it's all good.

## An awesome reason to use Conda
So, if you create an environment it is portable across projects: this is actually
awesome because you only need to `pip install` once. Projects that do different things
but use the same set of requirements can use the same environment.

# Outside-in Testing
Thinking about how to run in FAKE mode and REAL mode, I realised that I was "running 
the server" and clicking around, because that's really what this is - a `gradio` app
is a web page more than anything else. So I wasn't building test code.

So rather than keep stacking untested code upon untested code, I decided to pause for
a bit and make sure there is a way to provide proof that all the things work, not
just unit tests, but BDD style, browser-based tests.
