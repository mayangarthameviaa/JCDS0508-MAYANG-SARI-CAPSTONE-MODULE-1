# JCDS0508-MAYANG-SARI-CAPSTONE-MODULE-1

## Definition

Trust Pharmacy is a medication management system that allows users to display and purchase medications, as well as enables Admin to display, add, modify, and delete medications.

## Notes
The authentication for admin is: 

**username: Admin1**
**password: Pass1**

While for the user is: 

**username: User1**
**password: Pass1**


## Key Features

1. **Display Medications (Admin and User) →** View all available medications, including information such as code, name, price, quantity, and expiration date.

   **Special Features:**

   - Display all medications
   - Display medications by code
   - Display medications by name
   - Return to the main features

2. **Add Medication (Admin) →** Admin can add new medications to the system.

   **Special Features:**

   - Add new medications based on medication code without allowing data redundancy
   - Return to the main features.

3. **Modify Medication (Admin) →** Admin can modify existing medication information.

   **Special Features:**

   - Modify medication data based on medication code.
   - Columns that can be modified include name, quantity, price, and expiration date; however, the number and medication code columns cannot be changed.

4. **Delete Medication (Admin) →** Admin can delete medications from the system.

   **Special Features:**

   - Delete medication data based on medication code.

5. **Purchase Medication (User) →** Users can purchase medications.

   **Special Features:**

   - Purchase medications based on the name
   - If the medication is available, it will be added to the shopping cart, and the total amount will be displayed.
   - When the medication is successfully purchased, the stock of medication will decrease.

## Prerequisites

- Requires Python version 3.12.4
- Install the tabulate library in terminal using: `pip install tabulate`

## Installation

1. **Clone this repository**:
   ```bash
   bash
   Copy code
   git clone https://github.com/mayangarthameviaa/JCDS0508-MAYANG-SARI-CAPSTONE-MODULE-1.git
   ```

## Contact

- GitHub: mayangarthameviaa
- Email: mayangarthameviaa@gmail.com
