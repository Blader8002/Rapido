# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import regularizers
import tensorflow as tf

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
llama = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")

max_len = 128

def get_data(full):
    x_train = tokenizer(
        text=full[:450000],
        add_special_tokens=True,
        max_length=128,
        truncation=True,
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids=False,
        return_attention_mask=True,
        verbose=True
    )

    x_validation = tokenizer(
        text=full[8000:9000],
        add_special_tokens=True,
        max_length=256,
        truncation=True,
        padding=True,
        return_tensors='tf',
        return_token_type_ids=False,
        return_attention_mask=True,
        verbose=True
    )

    x_test = tokenizer(
        text=full[450000:],
        add_special_tokens=True,
        max_length=128,
        truncation=True,
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids=False,
        return_attention_mask=True,
        verbose=True
    )
    return x_train, x_validation, x_test


def get_model(llama):
    input_ids = Input(shape=(max_len,), dtype=tf.int32, name='input_ids')
    input_mask= Input(shape=(max_len,), dtype=tf.int32, name='attention_mask')

    embeddings = llama(input_ids,attention_mask=input_mask)[0]
    out= tf.keras.layers.GlobalMaxPool1D()(embeddings)
    out = Dense(128,activation='relu')(out)
    out = tf.keras.layers.Dropout(0.5)(out)
    out = Dense(16,activation='relu',kernel_regularizer=regularizers.l2(0.01))(out)
    out = tf.keras.layers.Dropout(0.5)(out)
    y = Dense(3,activation='softmax')(out)

    new_model = tf.keras.Model(inputs=[input_ids, input_mask], outputs=y)
    new_model.layers[2].trainable = True

    return new_model
