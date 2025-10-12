#!/usr/bin/env python3
"""
General and Computing Expense Reimbursement Manager
Helps Dr. Simon Wang manage and organize expense submissions to Google Sheets
"""

import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

# Add the Google API reusable path
api_path = "/Users/simonwang/Documents/Usage/VibeCodingMac/DailyAssistant/projects/GCAP3226/98_technical/google_api_reusable"
sys.path.append(api_path)

try:
    from secure_auth import GoogleAPIManager
except ImportError:
    print("❌ Could not import GoogleAPIManager. Please check the path.")
    print(f"Looking in: {api_path}")
    sys.exit(1)
from googleapiclient.discovery import build
import logging
from datetime import datetime
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExpenseReimbursementManager:
    """Manage general and computing expense reimbursements"""
    
    def __init__(self):
        self.auth_manager = GoogleAPIManager()
        self.credentials: Optional[Any] = None
        self.sheets_service: Optional[Any] = None
        self.drive_service: Optional[Any] = None
        
        # Google Sheets ID from your note
        self.spreadsheet_id = "1oAnEsLddX2abWS4QBXbDtGOYOpePJ7c3vPCcgOFh47A"
        self.sheet_name = "Sheet1"  # Update if different
        
    def initialize_services(self):
        """Initialize Google API services"""
        try:
            self.credentials = self.auth_manager.get_credentials()
            self.sheets_service = build('sheets', 'v4', credentials=self.credentials)
            self.drive_service = build('drive', 'v3', credentials=self.credentials)
            logger.info("✅ Google API services initialized")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to initialize services: {e}")
            return False
    
    def read_current_expenses(self):
        """Read current expenses from the Google Sheet"""
        try:
            if not self.sheets_service:
                logger.error("Sheets service not initialized")
                return []
            
            # Read the entire sheet to understand structure
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:Z"  # Read all columns
            ).execute()
            
            values = result.get('values', [])
            
            if not values:
                logger.warning("No data found in spreadsheet")
                return []
            
            logger.info(f"📊 Found {len(values)} rows in spreadsheet")
            
            # Display current structure
            print("\n📋 Current Spreadsheet Structure:")
            for i, row in enumerate(values[:5]):  # Show first 5 rows
                print(f"Row {i+1}: {row}")
            
            return values
            
        except Exception as e:
            logger.error(f"❌ Failed to read expenses: {e}")
            return []
    
    def add_expense_item(self, expense_data: Dict[str, str]) -> bool:
        """Add a new expense item to the sheet"""
        try:
            if not self.sheets_service:
                logger.error("Sheets service not initialized")
                return False
            
            # Prepare the row data based on typical expense sheet structure
            row_data = [
                expense_data.get('date', ''),
                expense_data.get('description', ''),
                expense_data.get('category', ''),
                expense_data.get('amount', ''),
                expense_data.get('currency', 'HKD'),
                expense_data.get('receipt_status', 'Pending'),
                expense_data.get('notes', ''),
                expense_data.get('reimbursement_status', 'Submitted')
            ]
            
            # Append to the sheet
            request = self.sheets_service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:H",
                valueInputOption='USER_ENTERED',
                body={'values': [row_data]}
            )
            
            result = request.execute()
            logger.info(f"✅ Added expense item: {expense_data.get('description')}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to add expense: {e}")
            return False
    
    def batch_add_expenses(self, expenses_list: List[Dict[str, str]]) -> bool:
        """Add multiple expenses at once"""
        try:
            if not expenses_list:
                logger.warning("No expenses to add")
                return False
            
            if not self.sheets_service:
                logger.error("Sheets service not initialized")
                return False
            
            # Prepare batch data
            rows_data = []
            for expense in expenses_list:
                row_data = [
                    expense.get('date', ''),
                    expense.get('description', ''),
                    expense.get('category', ''),
                    expense.get('amount', ''),
                    expense.get('currency', 'HKD'),
                    expense.get('receipt_status', 'Pending'),
                    expense.get('notes', ''),
                    expense.get('reimbursement_status', 'Submitted')
                ]
                rows_data.append(row_data)
            
            # Batch append
            request = self.sheets_service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:H",
                valueInputOption='USER_ENTERED',
                body={'values': rows_data}
            )
            
            result = request.execute()
            logger.info(f"✅ Added {len(expenses_list)} expense items")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to batch add expenses: {e}")
            return False
    
    def create_expense_folder(self, folder_name: str = "LANG2077_Expense_Receipts") -> Tuple[Optional[str], Optional[str]]:
        """Create a folder in Google Drive for receipt uploads"""
        try:
            if not self.drive_service:
                logger.error("Drive service not initialized")
                return None, None
            
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            
            folder = self.drive_service.files().create(body=file_metadata,
                                                     fields='id').execute()
            
            folder_id = folder.get('id')
            logger.info(f"✅ Created folder: {folder_name} (ID: {folder_id})")
            
            # Make folder shareable
            permission = {
                'type': 'anyone',
                'role': 'reader'
            }
            
            if self.drive_service:
                self.drive_service.permissions().create(
                    fileId=folder_id,
                    body=permission
                ).execute()
            
            folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
            logger.info(f"📁 Folder URL: {folder_url}")
            
            return folder_id, folder_url
            
        except Exception as e:
            logger.error(f"❌ Failed to create folder: {e}")
            return None, None
    
    def generate_expense_template(self):
        """Generate a template for adding expenses"""
        template_expenses = [
            {
                'date': '2024-09-27',
                'description': 'Computing Equipment - Example',
                'category': 'Computing',
                'amount': '1000.00',
                'currency': 'HKD',
                'receipt_status': 'Uploaded',
                'notes': 'Add your notes here',
                'reimbursement_status': 'Submitted'
            },
            {
                'date': '2024-09-26',
                'description': 'Office Supplies - Example',
                'category': 'General',
                'amount': '500.00',
                'currency': 'HKD',
                'receipt_status': 'Pending',
                'notes': 'Receipt to be uploaded',
                'reimbursement_status': 'Draft'
            }
        ]
        
        return template_expenses
    
    def display_summary(self):
        """Display current expense summary"""
        expenses = self.read_current_expenses()
        
        if not expenses:
            print("📊 No expenses found")
            return
        
        print(f"\n📊 EXPENSE SUMMARY")
        print("=" * 50)
        print(f"Total entries: {len(expenses)}")
        
        # Try to calculate totals (assuming amount in column D)
        total_amount = 0
        for i, row in enumerate(expenses[1:], 2):  # Skip header
            if len(row) > 3:  # Has amount column
                try:
                    amount = float(str(row[3]).replace(',', '').replace('$', ''))
                    total_amount += amount
                except:
                    pass
        
        print(f"Estimated total: ${total_amount:,.2f}")
        print("\n📋 Recent entries:")
        
        # Show last 5 entries
        for i, row in enumerate(expenses[-5:], len(expenses)-4):
            if len(row) > 1:
                desc = row[1] if len(row) > 1 else "No description"
                amount = row[3] if len(row) > 3 else "No amount"
                print(f"  {i}: {desc} - {amount}")

def main():
    """Main function for expense management"""
    print("💰 General and Computing Expense Reimbursement Manager")
    print("=" * 60)
    print("👤 User: Dr. Simon Wang")
    print("🏫 Institution: Hong Kong Baptist University")
    print("📊 Project: LANG2077 Finance Management")
    print("=" * 60)
    
    manager = ExpenseReimbursementManager()
    
    # Initialize services
    if not manager.initialize_services():
        print("❌ Failed to initialize. Check your Google API setup.")
        return
    
    # Display current summary
    manager.display_summary()
    
    # Create receipt folder
    print(f"\n📁 Creating receipt folder...")
    folder_id, folder_url = manager.create_expense_folder()
    
    if folder_id:
        print(f"✅ Receipt folder created: {folder_url}")
    
    # Generate template for new expenses
    print(f"\n📝 Expense template generated:")
    template = manager.generate_expense_template()
    for i, expense in enumerate(template, 1):
        print(f"\nTemplate {i}:")
        for key, value in expense.items():
            print(f"  {key}: {value}")
    
    print(f"\n🚀 Ready for expense management!")
    print(f"📊 Spreadsheet: https://docs.google.com/spreadsheets/d/{manager.spreadsheet_id}")
    print(f"📁 Receipt folder: {folder_url if folder_url else 'Create manually'}")

if __name__ == "__main__":
    main()