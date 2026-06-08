Name : Sitaram
Thiranex-internship Task-1 : Data Cleaning & Dual-Axis Visualization
Step 1: Loading the Data
•	What we did: The script looks for your CSV data file (raw_data.csv) and loads it into Python's memory using a tool called Pandas.
•	Why it matters: It automatically builds a preview so you can check how the raw numbers look before making changes.
Step 2: Fixing Missing & Broken Information
•	What we did: The script scans every single column for blank spaces (null values). If it finds a missing number, it fills it with the middle value (median) of that column. If a piece of text is missing, it labels it as "Unknown".
•	Why it matters: Blank spaces cause software crashes and math errors during calculations.
Step 3: Deleting Duplicate Information
•	What we did: The script hunts for identical rows that accidentally got repeated and permanently deletes them.
•	Why it matters: Duplicates distort real results (for example, counting the same airline passenger twice makes sales look higher than they actually are).
Step 4: Saving and Smart Plotting
•	What we did: The clean data is saved into a brand-new file called cleaned_data.csv. Then, the script automatically picks out the data to create a side-by-side, dual-axis bar chart.
•	Why it matters: You can instantly see your trends visually without overwriting or ruining your original raw data file.


What is Data Cleaning?
Think of data cleaning like washing vegetables before cooking. Raw data collected from the internet or business apps is almost always dirty—it has missing pieces, typos, and repeated entries. Data Cleaning is the process of fixing or removing these errors so your business decisions are based on accurate, trustworthy facts.
What is a Dual-Axis Chart?
A normal chart has one baseline (X-axis) and one vertical measurement line (Y-axis). A Dual-Axis Chart adds a second vertical measurement line on the right side.
Example: Imagine comparing Monthly Airline Passengers (numbers in the thousands) against Ticket Prices (numbers in the hundreds). If you put them on the same axis, the ticket price bars would look tiny and impossible to read. By giving them their own independent left and right scales, both metrics fit perfectly side-by-side on the same chart.
Python tools used : 
•	Pandas: The "Excel of Python." It allows us to hold data tables, filter rows, find empty spots, and save files instantly.
•	Matplotlib: The digital artist tool. It draws the chart frames, places the colorful bars, adjusts the fonts, and displays the final visual graphics on your screen.
Output:  
 <img width="855" height="919" alt="image" src="https://github.com/user-attachments/assets/8f7f9fa7-311b-4616-9326-fbd33c91ac4f" />

<img width="940" height="475" alt="image" src="https://github.com/user-attachments/assets/06e0972e-94ab-4dce-9e6c-2d217137c15b" />
