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

### vLLM

Before you run `pip install -r requirements.txt` you can comment out the line
which declares `vLLM` as a dependency. Then, clone the vllm repository and 
install vllm direct to the conda environment using `pip install -e .`

```
conda create -yn helpful-assistants python=3.11
conda activate helpfful-assistants
cd ~/Code/github/vllm
pip install -e .
cd -

pip install -r requirements.txt
```

The above is a pattern that could be applied to many of this project's dependencies.
If you want to bring all the repositories down locally and install them 'editable' (the `-e` flag in `pip install -e .`) simply remove those entries from the requirements.txt file before you install _helpful-assistants_.

[x] TODO: re-write this section so it is clearer



## Running the thing

```shell
# to run the server
make openai
# to run the client
make gradio
```

There are other options in the `Makefile` too, for running using
vLLM, textgen, and for serving other models through the openai REST API.


---

>what is the second verse of kubla khan

The second verse of "Kubla Khan" by Samuel Taylor Coleridge is as follows:
"And there were gardens bright with swift-future flowers,/ But even the air was laced with death/ And the cold light of the stars/ Made the pale grass and the fetters rust/ And all the world was old."
    

---


## The Makefile

The Makefile contains some patterns for running one or more servers, and testing the output.
These scripts are smoke tests, to ensure the servers are up and running etc.

To use the default model (dolphin-2.2.1-mistral-7b) run these commands. If you have more than two GPUs
you'll need to add them to [scripts/vllm-openai.mak](scripts/vllm-openai.mak). The PORT will need to be
set in the lines you copy and paste.
```
make openai-device-0
make openai-device-1
```

To run a test against the new LLM cluster use these commands.

```
make test-prompt-0 & make test-prompt-1 &
```

The above will fire up two servers simultaneously, occupying GPU 0 and 1. It's cool to watch
`nvtop` while this is happening.

There are some other scripts in the `scripts` folder too, for spinning up a new server and prompting running servers. The [Gum](https://github.com/charmbracelet/gum) cli tool is making things fun on the terminal.

## Getting a sense of GPU memory management.

Running a "cluster" of models begins to look like a tetris-clone. The shapes of each model are basically rectangular
but the trick is to keep at least 4G free for inference. The models with larger context require even more inference
VRAM.

So putting together a set of models ready for swarming:

```

```

## Code Organisation

The code started as a compact little tool to capture human input, send it to openai and display the response. As my
plans grew, so too did the complexity of the code, and considering all I had added was a bit of logging and the
ability to swap in a fake API client for testing, it's clear that Big Balls of Mud (BBOMs) are very easy to create.

Discipline in Source Code Arrangement: naming things and grouping responsibilities, declaring dependencies that are
required instead of instantiating them, controlling the composition of those dependencies from above to make testing
and configuration easier, limiting the scope of any given component's responsibility to make the code for that component
easier to reason about and reducing the cognitive draw overall.

By identifying the absence of Discipline in Source Code Arrangement

**TODO**:
* LHS Sidebar with "Characters" / "Archetypes"
  1. Each character is some kind of "expert"
  2. Each expert provides the system prompt e.g. "You are a scientist" or "You are a literary expert"
  3. Each expert has access to a "local knowledge repository" which is used to raise the level of knowledge each expert has access to
* Using a technique I'm calling **"Prompt Enrichment"** the expert resides on the user's machine
  The human submits a question which is interpreted by the sidecar LLM which then re-writes the question and optimises
  it for submission to the "big LLM" (say, ChatGPT)
* Prompt Enrichment uses another technique I'm calling **"Memory Compression"** where the history of the conversation is
  summarised and prepended to the submission for the big LLM, which achieves two things:
  1. Reduced cost of submission - fewer tokens sent to the big LLM
  2. Focused submission - removing extraneous words and using summarisation to maintain context 
* Testing:
  1. **Behave** for standardised behaviour assurance
  2. **Playwright** for browser control
  3. **unittest** for atomic assurance of code constructs

This is an experiment to see how alterations to system prompt change the way ChatGPT responses to questions differ
based on the system prompt. It is also an attempt to build a tool which brings focus and extra power to a user's
interactions with big LLMs by combining the user's line of inquiry with an AI's expertise in knowledge management and
speed of retrieval.

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
