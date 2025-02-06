# Counterfeit Product Detection Using Blockchain
# Overview

The Counterfeit Product Detection Using Blockchain project is a system designed to authenticate products and eliminate counterfeit goods by using blockchain technology. The system allows users to add product details, authenticate product scans, and retrieve product data based on the product ID. It ensures the integrity of product information and uses the immutability of blockchain to prevent fraud.

The application was developed using Python and Tkinter for the graphical user interface (GUI). The blockchain implementation is managed via the Blockchain.py and Block.py files, which handle the creation, validation, and storage of blocks containing product details.

This project provides a robust solution to ensuring that products are authentic and that consumers are not misled by counterfeits.
This was our final year project in our undergraduate degree which we presented in our class in may 2023. We are updating it in github now.

# Features

1. Add New Product:
  Users can add new products by entering product details such as ID, name, company/user details, and address.
A digital signature of the product is generated using the product's barcode. Product details are stored in a blockchain, and a new block is added to the chain with a unique hash for verification.
2. Authenticate Product:
  Users can authenticate a product by scanning its barcode. The barcode's digital signature is checked against the blockchain to confirm the product’s authenticity.
3. Search Product by ID:
  Users can search for a product by its unique ID. If the product exists in the blockchain, all the details stored on the blockchain are displayed.
4. Blockchain Implementation:
  The blockchain consists of blocks that store transactions related to product details. Each block contains the product ID, name, user/company details, and a digital signature. The blockchain ensures immutability, preventing any tampering with the product data.
5. User Interface:
  The application uses a simple, intuitive GUI created with Tkinter. It allows users to add products, authenticate products, and search for product details. The GUI is designed to be clear and user-friendly, with centered inputs and larger buttons for ease of interaction.

# Mechanics and Features

# Blockchain Components

1. Block Class (Block.py):
  Defines a block in the blockchain, containing product transactions, previous block hash, timestamp, and a digital signature.
2. Blockchain Class (Blockchain.py):
   Manages the blockchain by adding blocks, mining, and saving the blockchain state. It includes a proof-of-work mechanism to secure the blockchain.

# Product Addition

  Product details are added to the blockchain by entering the product ID, name, user/company details, and address.
A digital signature of the product is generated using its barcode, ensuring its authenticity.
New product transactions are added to the blockchain and stored permanently.

# Product Authentication
  The system allows the user to authenticate a product by scanning its barcode.
The digital signature is checked against the blockchain to verify the product’s authenticity.

# Product Search

  Users can search for a product by its ID. If the product exists in the blockchain, its details are retrieved and displayed.
  
# Setup and Installation

# Prerequisites
1. Python 3.x
2. Tkinter (for GUI)
3. hashlib (for creating the digital signature)
4. Pickle (for serializing blockchain data)

# Instructions

1. Clone or download the project to your local machine.
2. Install Python and the required dependencies if they are not already installed.
3. Run the run.bat/run.sh script depending on your PC (run.bat for windows/unix and run.sh for MacOS)to launch the application.

# Running the Application
1. To Add a Product:
   Enter the product details and click the Save Product with Blockchain Entry button.
2. To Authenticate a Product:
   Click Authenticate Scan, scan the barcode, and verify if the product is authentic.
3. To Retrieve Product Data:
   Enter the product ID and click Retrieve Product Data to see the details of the product stored in the blockchain.

# Authors

[Sriya Choudary Yalavarthy](https://github.com/sriya632)

Gayathri Tummala

# Assets

UI: Custom UI components for product input and display.
Blockchain: Uses Python's built-in hashlib for generating digital signatures.
