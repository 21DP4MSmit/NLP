from transformers import pipeline

def main():
    print("Debug: Initializing GPT-2 text generation pipeline...")
    try:
        generator = pipeline("text-generation", model="gpt2")
        print("Debug: GPT-2 pipeline initialized successfully!")
    except Exception as e:
        print(f"Error initializing GPT-2 pipeline: {e}")
        return

    start_phrase = "Reiz kādā tālā zemē..."
    
    print("Debug: Generating text...")
    try:
        result = generator(
            start_phrase,
            max_length=100,
            num_return_sequences=1,  # Generate one sequence
            temperature=0.9,  # Control randomness; higher is more creative
            truncation=True
        )
        print("Ģenerētais teksts:")
        print(result[0]['generated_text'])
    except Exception as e:
        print(f"Error during text generation: {e}")
