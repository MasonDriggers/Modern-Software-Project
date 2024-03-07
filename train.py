from transformers import TrainingArguments


training_args = TrainingArguments(
    output_dir='./results',                # Directory for saving model and checkpoints
    num_train_epochs=3,                    # Number of training epochs
    per_device_train_batch_size=8,         # Batch size per device during training
    per_device_eval_batch_size=8,          # Batch size for evaluation
    warmup_steps=500,                      # Number of warmup steps for learning rate scheduler
    weight_decay=0.01,                     # Weight decay if we apply some.
    logging_dir='./logs',                  # Directory for logs
    logging_steps=10,                      # Log every X updates steps.
    evaluation_strategy="epoch",           # Evaluate at the end of every epoch
)
