# General and Computing Expense Reimbursement Action Plan
**For Dr. Simon Wang - HKBU LANG2077 Project**

## 🎯 IMMEDIATE PRIORITIES

### Google Spreadsheet Management
**Current Sheet**: https://docs.google.com/spreadsheets/d/1oAnEsLddX2abWS4QBXbDtGOYOpePJ7c3vPCcgOFh47A/edit?resourcekey=&gid=2098253691#gid=2098253691

#### Action Items:
- [ ] **Review current spreadsheet structure** and existing entries
- [ ] **List new expense items** in this document (see template below)
- [ ] **Upload receipt copies** to Google Drive folder
- [ ] **Submit completed items** via the form or spreadsheet

### Email Management
**NEWFIS Account**: newfis@hkbu.edu.hk
- [ ] **Download all reimbursement emails** from newfis account
- [ ] **Track reimbursement claim status** for each submission
- [ ] **Organize correspondence** by expense category

## 📋 EXPENSE ENTRY TEMPLATE

### Template for New Expenses:
```
Date: [YYYY-MM-DD]
Description: [Detailed description of expense]
Category: [General/Computing/Travel/Other]
Amount: [HK$XXX.XX]
Currency: [HKD/CNY/USD]
Receipt Status: [Original/Copy/Digital/Missing]
Vendor: [Company/Store name]
Purpose: [LANG2077 related justification]
Reimbursement Status: [Draft/Submitted/Processing/Approved/Paid]
Notes: [Additional information]
```

### Example Entries:
```
Date: 2024-09-27
Description: MacBook Pro for LANG2077 project development
Category: Computing
Amount: HK$15,000.00
Currency: HKD
Receipt Status: Original
Vendor: Apple Store Hong Kong
Purpose: Computing equipment for course development and student projects
Reimbursement Status: Draft
Notes: Required for video editing and programming tasks

Date: 2024-09-26
Description: Office supplies - stationery and printing
Category: General
Amount: HK$250.00
Currency: HKD
Receipt Status: Copy
Vendor: Commercial Press
Purpose: Course materials and administrative supplies
Reimbursement Status: Submitted
Notes: Monthly office supplies procurement
```

## 🗂️ ORGANIZATION STRUCTURE

### Create These Folders:
1. **LANG2077_Computing_Expenses**
   - Hardware purchases
   - Software licenses
   - Technical equipment

2. **LANG2077_General_Expenses**
   - Office supplies
   - Administrative costs
   - Miscellaneous items

3. **LANG2077_Receipt_Archive**
   - Original receipt scans
   - Vendor invoices
   - Payment confirmations

### File Naming Convention:
- **[YYYY-MM-DD]_[Category]_[Description]_[Amount].pdf**
- Example: `2024-09-27_Computing_MacBookPro_15000HKD.pdf`

## 🚀 AUTOMATED TOOLS SETUP

### Using Google API Tools:
The Python script `General_Computing_Expense_Manager.py` can help with:
- **Automated spreadsheet updates**
- **Batch expense entry**
- **Receipt folder organization**
- **Status tracking**

### Setup Instructions:
1. **Navigate to API directory**:
   ```bash
   cd "/Users/simonwang/Documents/Usage/VibeCodingMac/DailyAssistant/projects/GCAP3226/98_technical/google_api_reusable"
   ```

2. **Run the expense manager**:
   ```bash
   python3 "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/LANG2077/financeFollowUp/General_Computing_Expense_Manager.py"
   ```

## 📊 TRACKING DASHBOARD

### Key Metrics to Monitor:
- [ ] **Total expenses submitted**: $XXX,XXX.XX
- [ ] **Pending approvals**: $XX,XXX.XX
- [ ] **Processing time**: X days average
- [ ] **Outstanding receipts**: X items

### Status Categories:
1. **Draft** - Expense identified, not yet submitted
2. **Submitted** - Sent to finance office
3. **Processing** - Under review
4. **Approved** - Waiting for payment
5. **Paid** - Reimbursement received
6. **Rejected** - Requires action/resubmission

## ⚠️ COMMON ISSUES & SOLUTIONS

### Receipt Problems:
- **Missing original receipts**: Contact vendor for duplicate
- **Damaged receipts**: Submit copy with explanation letter
- **Foreign language receipts**: Provide English translation

### Approval Delays:
- **Follow up weekly** with finance office
- **Provide additional documentation** if requested
- **Escalate to Dr. Cissy Li** if necessary

### Technical Issues:
- **Spreadsheet access problems**: Check Google account permissions
- **Form submission errors**: Try direct spreadsheet entry
- **File upload failures**: Reduce file size or change format

## 📧 COMMUNICATION TEMPLATES

### Status Inquiry Email:
```
Subject: LANG2077 Expense Reimbursement Status Inquiry

Dear [Finance Officer],

I would like to inquire about the status of my expense reimbursement submissions for the LANG2077 project.

Submission details:
- Date submitted: [Date]
- Amount: HK$[Amount]
- Reference number: [If available]

Could you please provide an update on the processing status?

Thank you for your assistance.

Best regards,
Dr. Simon Wang
Hong Kong Baptist University
```

## 🎯 NEXT STEPS

### This Week:
- [ ] **List all pending expenses** using the template above
- [ ] **Organize existing receipts** into categories
- [ ] **Set up Google Drive folders** for receipt storage

### Next Week:
- [ ] **Submit organized expenses** to spreadsheet
- [ ] **Upload all receipt copies** to Drive folders
- [ ] **Follow up** on pending reimbursements

### Ongoing:
- [ ] **Weekly status checks** with finance office
- [ ] **Monthly expense summary** reporting
- [ ] **Receipt backup** to multiple locations

---

**📝 ADD YOUR NEW EXPENSE ITEMS BELOW:**

*Use the template above to list any new expenses you need to submit...*