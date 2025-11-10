#!/usr/bin/env python3
"""
Simple runner for General and Computing Expense Management
Dr. Simon Wang - HKBU LANG2077 Project
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Run the expense management tools"""
    print("💰 LANG2077 Expense Management Runner")
    print("=" * 50)
    print("👤 Dr. Simon Wang - Hong Kong Baptist University")
    print()
    
    # Define paths
    api_path = "/Users/simonwang/Documents/Usage/VibeCodingMac/DailyAssistant/projects/GCAP3226/98_technical/google_api_reusable"
    expense_manager_path = "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/LANG2077/financeFollowUp/General_Computing_Expense_Manager.py"
    
    # Check if Google API tools exist
    if not Path(api_path).exists():
        print(f"❌ Google API tools not found at: {api_path}")
        print("Please check the path and try again.")
        return
    
    # Check if expense manager exists
    if not Path(expense_manager_path).exists():
        print(f"❌ Expense manager not found at: {expense_manager_path}")
        return
    
    print("📋 Available Actions:")
    print("1. Test Google API connection")
    print("2. Run expense manager")
    print("3. Open Google Spreadsheet")
    print("4. Show action plan")
    print("5. Exit")
    print()
    
    while True:
        choice = input("Select an action (1-5): ").strip()
        
        if choice == "1":
            print("\n🔍 Testing Google API connection...")
            try:
                # Change to API directory and run test
                os.chdir(api_path)
                result = subprocess.run([sys.executable, "secure_auth.py"], 
                                      capture_output=True, text=True)
                print(result.stdout)
                if result.stderr:
                    print(f"Errors: {result.stderr}")
            except Exception as e:
                print(f"❌ Error testing connection: {e}")
        
        elif choice == "2":
            print("\n🚀 Running expense manager...")
            try:
                # Run the expense manager
                result = subprocess.run([sys.executable, expense_manager_path], 
                                      capture_output=True, text=True)
                print(result.stdout)
                if result.stderr:
                    print(f"Errors: {result.stderr}")
            except Exception as e:
                print(f"❌ Error running expense manager: {e}")
        
        elif choice == "3":
            print("\n📊 Opening Google Spreadsheet...")
            spreadsheet_url = "https://docs.google.com/spreadsheets/d/1oAnEsLddX2abWS4QBXbDtGOYOpePJ7c3vPCcgOFh47A/edit?resourcekey=&gid=2098253691#gid=2098253691"
            
            try:
                # Try to open in browser
                import webbrowser
                webbrowser.open(spreadsheet_url)
                print("✅ Spreadsheet opened in browser")
            except Exception as e:
                print(f"❌ Could not open browser: {e}")
                print(f"📋 Manual URL: {spreadsheet_url}")
        
        elif choice == "4":
            print("\n📋 Action Plan Location:")
            action_plan_path = "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/LANG2077/financeFollowUp/General_Computing_Expense_Action_Plan.md"
            print(f"📁 {action_plan_path}")
            
            try:
                # Try to open the action plan
                subprocess.run(["open", action_plan_path])
                print("✅ Action plan opened")
            except Exception as e:
                print(f"❌ Could not open action plan: {e}")
        
        elif choice == "5":
            print("\n👋 Goodbye! Good luck with your expense management.")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-5.")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main()