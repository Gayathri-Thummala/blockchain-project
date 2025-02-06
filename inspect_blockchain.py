import pickle

# Load the blockchain from the file
with open('blockchain_contract.txt', 'rb') as file:
    blockchain = pickle.load(file)

# Print the blockchain details
for block in blockchain.chain:
    print(f"Block No: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Current Hash: {block.hash}")

    # Iterate over each transaction in the block
    for transaction in block.transactions:
        # Split the transaction string into product details
        details = transaction.split("#")
        if len(details) >= 6:
            pid = details[0]
            name = details[1]
            user = details[2]
            address = details[3]
            timestamp = details[4]
            digital_signature = details[5]

            # Print the product details
            print(f"Product ID             : {pid}")
            print(f"Product Name           : {name}")
            print(f"Company/User Details   : {user}")
            print(f"Address Details        : {address}")
            print(f"Scan Date & Time       : {timestamp}")
            print(f"Product Barcode Digital Sign : {digital_signature}")
            print("=" * 40)  # Separator for better readability
        else:
            print("Invalid transaction data!")
    print("\n")
