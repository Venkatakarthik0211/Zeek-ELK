## Deep Learning

- **Artificial Neural Network (ANN)**: This is a computational model based on the structure of a human's neural system. It consists of interconnected nodes or "neurons" that process information. It's used for tasks like image recognition, speech recognition, and making predictions.

- **Convolutional Neural Network (CNN)**: This is a type of ANN designed to process grid-structured data, like images. It's particularly good at recognizing patterns in the input data.

- **Recurrent Neural Network (RNN)**: This is a type of ANN where connections between nodes form a directed graph along a sequence. This allows it to use its internal state (memory) to process sequences of inputs, making it ideal for tasks like language modeling and translation.

1. **LSTM (Long Short-Term Memory)**: LSTM is a type of recurrent neural network (RNN) architecture that is designed to overcome the vanishing gradient problem by introducing memory cells and gating mechanisms. It is commonly used for tasks involving sequential data, such as natural language processing and speech recognition.

2. **GRU (Gated Recurrent Unit)**: GRU is another type of recurrent neural network (RNN) architecture that is similar to LSTM but has a simplified structure with fewer gating mechanisms. It is also used for tasks involving sequential data and is known for its computational efficiency.

`Mote: ` LSTM and GRU differ from traditional RNNs in that they have additional mechanisms, such as **memory cells** and **gating mechanisms**, which allow them to capture and retain information over longer sequences. This makes them better suited for tasks that involve long-term dependencies and mitigates the vanishing gradient problem. Additionally, LSTM has separate memory cells and gating mechanisms, while GRU combines them into a single update gate, making it computationally more efficient. Overall, LSTM and GRU are more powerful and flexible than traditional RNNs, enabling them to handle more complex sequential data. 

- **Seq2seq modal:** https://www.geeksforgeeks.org/seq2seq-model-in-machine-learning/ 
- **Attention** https://www.geeksforgeeks.org/ml-attention-mechanism/ 

- **Reinforcement Learning**: This is a type of machine learning where an agent learns to make decisions by taking actions in an environment to achieve a goal. The agent learns from the consequences of its actions, rather than from being explicitly taught.

- **Gain**: In the context of machine learning, gain often refers to the improvement in accuracy or predictive power that a model achieves from learning a feature. It's a measure of the usefulness of a feature in the model.

## Artificial Intelligence

- **Generative AI:** Generative AI refers to a class of machine learning models that have the ability to generate new and original content, such as images, music, or text. These models are trained on large datasets and learn to capture the underlying patterns and structures in the data, allowing them to generate realistic and coherent outputs. Generative AI has applications in various fields, including art, design, and content creation, and is a rapidly evolving area of resea rch in the field of artificial intelligence. It is a subset of **Deep Learning**
Ex: Gen Image models, Gen Langague models. 

- **Discriminative AI:** Discriminative AI refers to a class of machine learning models that focus on learning the boundary between different classes or categories of data, enabling them to classify new instances based on their features and characteristics.

- **Transfer Learning:** Transfer learning is a machine learning technique where knowledge gained from training one model is applied to a different but related task or domain, typically speeding up training and improving performance.

## Large Langauge Modelss

Based on the tuning approach: 

- **Generic Langauge Models:** Generic language models are large-scale neural networks trained on extensive text data to predict and generate coherent sequences of language, capable of understanding and producing human-like text across a wide range of topics and contexts.
Ex: ChatGPT

- **Instruction tuning models:** Instruction tuning models are specialized machine learning models designed to optimize the performance and accuracy of assembly-level code by dynamically adjusting compiler optimizations and configurations based on program instructions, enhancing execution efficiency on specific hardware architectures.
Ex: Intel's Automatic Code Transforms (ACT)

- **Dialogue tuning modals:** Dialog tuning models are machine learning frameworks tailored to enhance conversational agents' performance by adapting responses based on ongoing interactions, aiming to improve dialogue quality, relevance, and user satisfaction in natural language processing tasks.
Ex: ChatBot

- **Domain specific tuning modals:** Domain-specific tuning models refer to machine learning approaches that customize models to excel in particular fields or contexts by fine-tuning parameters and training data, ensuring optimal performance and relevance within specialized domains like medicine, finance, or engineering.
Ex: AWS Comprehend

## Neural Network 

A neural network is a computational model inspired by the biological brain's interconnected neurons, comprising layers of nodes that process input data through weighted connections, enabling complex pattern recognition and learning tasks in machine learning and artificial intelligence applications.

- **Activation Function:** An activation function in a neural network is a mathematical function applied to the output of each neuron, determining whether it should be activated (produce an output) based on the weighted sum input received.

- **Generative Adversarial Network:** A Generative Adversarial Network (GAN) is a type of machine learning model consisting of two neural networks, the generator and the discriminator, which compete in a game-theoretic framework. The generator aims to generate realistic data samples, while the discriminator learns to distinguish between generated and real data, resulting in improved generation of synthetic data resembling real-world examples.

## Transformers
A Transformer is a deep learning model architecture designed for processing sequential data, utilizing self-attention mechanisms to capture relationships between input elements across varying distances without recurrence, making it highly efficient for tasks such as natural language processing.

**Encoder:**
An Encoder in the Transformer architecture processes input data by transforming it into a series of abstract representations using multi-head self-attention and feedforward neural networks, enabling comprehensive feature extraction from sequential data for downstream tasks like translation or summarization.

**Decoder:**
A Decoder in the Transformer architecture reconstructs output sequences from the abstract representations generated by the encoder, utilizing masked multi-head self-attention and cross-attention mechanisms to generate accurate predictions or translations based on learned contextual information.

**Self Attention:**
Self-attention is a mechanism in neural networks where each element in a sequence (e.g., words in a sentence) attends to other elements, learning weighted dependencies to better capture contextual relationships, crucial for tasks like natural language understanding and machine translation.

## Components of encoding and decoding 

- **Encoding components** (Self Attention and Feed forward)
- **Decoding components** (self attention, Encoder-Decoder Attention, feed forward)





