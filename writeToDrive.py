import gspread


def write_to_google_sheet(sherpaName, whenHelped, sherpalingName, time_spend, description, ticketTranscript):
    # Authorize with Google Sheets using OAuth2 with user account


    print(sherpaName)



    valuesToAppend = whenHelped,sherpalingName,time_spend,description,ticketTranscript

    gc = gspread.service_account()

    # Replace 'YOUR_SPREADSHEET_NAME' with the name of your Google Sheets document
    spreadsheet_name = 'Titled'

    # Open the spreadsheet
    spreadsheet = gc.open(spreadsheet_name)


    for x in spreadsheet:
        if x.title == sherpaName:
            tempId = x.index


    # Select the first worksheet (Temp1) by its title or index (e.g., 0 for the first sheet)
    worksheet = spreadsheet.get_worksheet(tempId)
    worksheet.append_row(valuesToAppend)




