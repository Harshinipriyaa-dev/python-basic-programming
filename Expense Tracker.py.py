import mysql.connector
import csv
from datetime import datetime

# setting up
DB_NAME = 'expense_tracker'
TABLE_NAME = 'expenses'
DB_USER = 'root'      
DB_PASSWORD = 'Harsh@11'  
DB_HOST = 'localhost'

# connecting to database
def connect_db():
    
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.database = DB_NAME

    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(255),
            description TEXT,
            amount DECIMAL(10, 2)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# connecting with sql
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# adding expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
            cat = int(input('''
                                       1.🙋🏾Essentials & Living:                                                                  2.🚗 Transportation         
                                                        >Groceries                                                                            >Fuel / Petrol / Diesel  
                                                        >Rent / Mortgage                                                                      >Public Transport
                                                        >Utilities (electricity, water, gas)                                                  >Vehicle Maintenance     
                                                        >Internet / Wi-Fi                                                                     >Insurance (Vehicle) 
                                                        >Mobile / Phone                                                                 
                                                        >House Maintenance / Repairs

                                         3.🍽 Food & Dining                                                                     4.💡 Personal & Family
                                                       >Eating Out / Restaurants                                                         >Clothing                                                                   >Fitness / Gym / Yoga
                                                       >Takeaway / Delivery                                                              >Healthcare / Medicines                                        >Education / Tuition
                                                       >Snacks / Beverages                                                               >Personal Care (salon, grooming, etc.)              >Childcare / Kids' Needs  
                                       
                                         5. 🏦 Finance & Bills                                                                  6.  🎉 Entertainment & Leisure
                                                         >Loan EMI                                                                     >Streaming Services (Netflix, Spotify, etc.)
                                                         >Credit Card Payments                                                         >Movies / Events 
                                                         >Insurance Premiums                                                           >Hobbies 
                                                         >Savings / Investments                                                        >Trips / Travel               

                                          7.  🎁 Gifts & Donations                                                               8.  🛍 Shopping & Misc        
                                                        >Gifts / Presents                                                                >Home Supplies (cleaning, kitchen tools, etc.)
                                                        >Charity / Donations                                                             >Electronics / Gadgets 
                                                        >Festive Spending                                                                >Miscellaneous
                                                        
         ------->   SELECT CATEGORY  (enter number of preffered category) : '''))
        if cat==1:
            category='Essentials & Living'
        elif cat==2:
            category='Transportation'
        elif cat==3:
            category='Food & Dining'
        elif cat==4:
            category='Personal & Family'
        elif cat==5:
            category='Finance & Bills'
        elif cat==6:
            category='Entertainment & Leisure'
        elif cat==7:
             category='Gifts & Donations'
        elif cat==8:
             category='Shopping & Misc'
        else:
            category='custom                             '
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (date, category, description, amount)
            VALUES (%s, %s, %s, %s)
        """, (date, category, description, amount))
        conn.commit()
        print('-'*185)
        print("                                                                                                                                                ✅ Expense added.\n")
        print('-'*185)
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

# viewing expense
def view_expenses():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY date DESC")
        rows = cursor.fetchall()

        if not rows:
            print('-'*185)
            print("\n 📭        Ｎｏ  ｅｘｐｅｎｓｅｓ  ｆｏｕｎｄ.\n")
            print('-'*185)
            return

        print('-'*185)
        print("\n🧾    ᗩᒪᒪ ᕮ᙭ᑭᕮᑎSᕮS:")
        print('-'*185)
        print(f"{'ID':<5} {'Date':<12}       {'Category':<20}          {'Amount':>30}                       {'Description':<60}")
        print("=" * 100)

        
        for row in rows:
            id = str(row[0])
            date = str(row[1])
            category = row[2][:18]  
            description = row[3][:20]  
            amount = f"₹{row[4]:.2f}"
            print(f"{id:<5} {date:<12} {category:<20}        {amount:>30}                          {description:<60}")
        
        print("=" * 100 + "\n")
    except Exception as e:
        print('-'*185)
        print('-'*185)
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()


# Update Expense 
def update_expense():
    try:
        expense_id = input("Enter Expense ID to update: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = %s", (expense_id,))
        row = cursor.fetchone()

        if not row:
            print("❌  Ｅｘｐｅｎｓｅ  ｎｏｔ  ｆｏｕｎｄ.\n")
            return
        print('-'*185)
        print("Leave blank to keep current value.")
        new_date = input(f"New date ({row[1]}): ") or row[1]
        new_category = input(f"New category ({row[2]}): ") or row[2]
        new_description = input(f"New description ({row[3]}): ") or row[3]
        new_amount = input(f"New amount ({row[4]}): ") or row[4]

        cursor.execute(f"""
            UPDATE {TABLE_NAME}
            SET date = %s, category = %s, description = %s, amount = %s
            WHERE id = %s
        """, (new_date, new_category, new_description, new_amount, expense_id))
        conn.commit()
        print('-'*185)
        print("                                                                                                                                                          ✅ Expense updated.\n")
        print('-'*185)
    except Exception as e:
        print('-'*185)
        print('-'*185)
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

# Delete Expense
def delete_expense():
    try:
        expense_id = input("Enter Expense ID to delete: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = %s", (expense_id,))
        conn.commit()
        if cursor.rowcount:
            print('-'*185)
            print("                                                                                                                                                         ✅ Expense deleted.\n")
            print('-'*185)
        else:
            print("❌  Ｅｘｐｅｎｓｅ  ｎｏｔ  ｆｏｕｎｄ.\n")
    except Exception as e:
        print('-'*185)
        print('-'*185)
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

#  Export to CSV 
def export_to_csv():
    try:
        filename = input("Enter filename to export (e.g., expenses.csv): ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cursor.fetchall()

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Date", "Category", "Description", "Amount"])
            writer.writerows(rows)
        print('-'*185)
        print(f"                                                                                                                                       ✅ Exported to {filename}\n")
        print('-'*185)
    except Exception as e:
        print('-'*185)
        print('-'*185)
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

#  Import from CSV
def import_from_csv():
    try:
        filename = input("Enter filename to import (e.g., expenses.csv): ")
        conn = get_connection()
        cursor = conn.cursor()

        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(f"""
                    INSERT INTO {TABLE_NAME} (date, category, description, amount)
                    VALUES (%s, %s, %s, %s)
                """, (row['Date'], row['Category'], row['Description'], row['Amount']))
        conn.commit()
        print('-'*185)
        print(f"                                                                                                                              ✅ Imported from {filename}\n")
        print('-'*185)
    except Exception as e:
        print('-'*185)
        print('-'*185)
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

#  Generating Report 
def generate_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT category, SUM(amount)
            FROM {TABLE_NAME}
            GROUP BY category
        """)
        rows = cursor.fetchall()
        print('-'*185)
        print('                                                                                                                      👀 TᖇᗩᑕK ᕮᐯᕮᖇY ᑭᕮᑎᑎY, GᖇOᗯ ᕮᐯᕮᖇY ᖇᑌᑭᑭᕮᕮ ')
        print('-'*185)
        print("\n📊      𝔼𝕩𝕡𝕖𝕟𝕤𝕖 ℝ𝕖𝕡𝕠𝕣𝕥 𝕓𝕪 ℂ𝕒𝕥𝕖𝕘𝕠𝕣𝕪:")
        print('\n')
        print("Category                | Total Amount")
        print("-" * 30)
        for row in rows:
            print(f"{row[0][:15]:<17}        ₹{row[1]:.2f}")
        print()
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cursor.close()
        conn.close()

# main program
def main():
    connect_db()  

    while True:
        print('-'*185)
        print('                                                                                    !!!  ~~~~  ＨＥＹ👋  _______    ＬＥＴＳ  ＴＲＡＣＫ  ＹＯＵＲ  ＥＸＰＥＳＥＳ  ~~~~  !!!')
        print('-'*185)
        print('\n')
        print('                                                                                           because every expense tells the story😇 ~~~ your money organized - optimized 💡')
        print('\n')
        print("================================================================================👉  Ⓔ̑Ⓧ̑Ⓟ̑Ⓔ̑Ⓝ̑Ⓢ̑Ⓔ̑   Ⓣ̑Ⓡ̑Ⓐ̑Ⓒ̑Ⓚ̑Ⓔ̑Ⓡ̑   Ⓜ̑Ⓔ̑Ⓝ̑Ⓤ̑   👈🏿 ===========================================================================================")
        print('\n')
        print(" PRESS  1  ---- >                                                                                 1. Add Expense")
        print(" PRESS  2 ---->                                                                                  2. View Expenses")
        print(" PRESS  3 ---->                                                                                  3. Update Expense")
        print(" PRESS  4 ---->                                                                                  4. Delete Expense")
        print(" PRESS  5 ---->                                                                                  5. Export to CSV")
        print(" PRESS  6 ---->                                                                                  6. Import from CSV")
        print(" PRESS  7 ---->                                                                                  7. Generate Report")
        print(" PRESS  8 ---->                                                                                  8. Exit")
        print('\n')
        print('-'*185)
        choice = input("Smart Spending Starts Here 🤗                                                      ----->  enter your choice: ")
        print('\n')

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            import_from_csv()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            print('-'*185)
            print('''                                                                                                                                     𝐇𝐢𝐭 𝐦𝐞 𝐮𝐩 𝐰𝐡𝐞𝐧 𝐲𝐨𝐮 𝐧𝐞𝐞𝐝 𝐦𝐞!!!''')
            print('                                                                                                      bᴜ𝚝 ɾᥱɱᥱɱbᥱɾ:    𝑾𝑨𝑻𝑪𝑯 ❤️ 𝒀𝑶𝑼𝑹 ❤️ 𝑾𝑨𝑳𝑳𝑬𝑻 ❤️ 𝑺𝑴𝑰𝑳𝑬 ❤️ 🛍 ')
            print('\n')
            print("                                                                                                                                             👋  G˶o˶o˶d˶b˶y˶e˶!       ")
            break
        else:
            print('-'*185)
            print("❌ Invalid choice. Try again.\n")
            print('-'*185)

if __name__ == "__main__":
    main()
