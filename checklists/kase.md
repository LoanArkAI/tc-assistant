# Kase checklists

Imported 2026-10-13 from `ck.xlsx` by `scripts/import_checklists.py` — edit the workbook and re-import rather than editing this file.

**Naming convention:** a filed document is named exactly as its checklist item below.

Legend: **req** = always required · `cond:…` = required when the deal carries that tag · *if applicable* = only if the document exists for this deal · *field* = a compliance-system field, not a document.

## KASE LISTING (Includes SFR/Condo)
`kase-listing-includes-sfr-condo` · 39 items

**Listing Documentation**

- BROKER NOTES · *field* — BROKER NOTES *
- TC For File - Please add your Name and email · *field*
- Preliminary Title Report · req
- Tax Record / Realist Report · req
- RLA - Residential Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- NHD REPORT · req
- AD - Agency Disclosure · req
- KASE Listing ADM · req
- SA - Seller Advisory · req
- BCA - Broker Compensation Advisory · req
- PRBS-S - Possible Rep of More than one Buyer or Sell · req
- FHDA - Fair Housing Discrimination Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- Coming Soon Form (MLS) · `cond:coming-soon`
- MLS Active - Full Agent Report · req
- DIA - Disclosure Information Advisory · req
- LPD - Lead-Based Paint Disclosure · `cond:pre1978`
- MT-LA - Modification of Terms, Listing Agreement · *if applicable*
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- TA - Trust Advisory · `cond:trust`
- Trust, Notarized Cert of Trust or Testamentary · `cond:trust` — Help Text: Testamentary only for Probate Listings
- RCSD-S - Representative Capacity Signature Disc · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust`
- RFA - Referral Fee Agreement · `cond:referral`
- FHDS - Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD Report shows High Fire Zone
- TDS- Seller Signed · req
- SPQ - Seller Signed · req
- ESD - Exempt Seller Disclosure · `cond:esd`
- SELI - Exclude Listing from Internet · `cond:off-internet`
- SPRP - Sellers Purchase of Replacement Property · `cond:replacement-property`
- SOLAR - Solar Questionnaire · `cond:solar`
- AVID - Seller/Listing Agent Signed · req
- 9a City Report · `cond:la-city` — If required by city.
- COC - Certificate of Compliance · req
- Miscellaneous - Listing · *if applicable*
- COL - Cancellation of Listing · `cond:canceled`

## KASE Purchase (Includes SFR/Condo)
`kase-purchase-includes-sfr-condo` · 115 items

**Sales Documentation**

- BROKER NOTES · *field*
- TC for File - Please add your name and email · *field*
- AD - Agency Disclosure (Buyer) · req
- RPA - Residential Purchase Agreement · req
- SMCO- Seller Multiple Counter Offer · `cond:counter`
- SCO - Seller Counter Offer(s) · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- BIA - Buyers Inspection Advisory · req
- AAA - Additonal Agent Acknowledgement · `cond:team`
- ABA - Additional Brokerage Acknowledgement · `cond:team`
- AC - Confirmation of Real Estate Agency · *if applicable*
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AEA - Amendment of Exisiting Terms · *if applicable*
- AOAA - Assignment of Agreement Addendum · *if applicable*
- BCA - Broker Compensation Advisory · req
- PRBS-B - Possible Rep more than one Buyer or Seller · req
- FHDA- Fair Housing Discrimination Advisory · req
- BHIA- Buyer Homeowners Insurance Advisory · req
- WFA - Wire Fraud Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- BRBC - Buyer Rep & Broker Compensation Agreement · `side:buy` — HELP: Only upload if representing Buyer
- EMD - Earnest Money Deposit · req
- ETA - Extension of Time Amendment · *if applicable*
- TIC-PA- Tenancy In Common Purchase Addendum · `cond:tic`
- PA-PA - Probate Purchase Addendum · `cond:probate`
- COP - Contingency of Sale of Buyers Property · `cond:contingent-sale`
- CR - Inspection · req
- CR - Appraisal · req
- CR - Loan · req
- CR - Removal of ALL Contingencies · req
- COOP-PA Stock Cooperative Purchase Addendum · `cond:coop`
- Escrow Acknowledgement (Page 17) · req
- Escrow Instructions · req
- Escrow Amendments · *if applicable*
- Escrow Commission Instructions w/Broker Signature · req
- Entity Docs (LLC or Corp) · `cond:trust`
- Trust, Notarized Certificate of Trust or Testamentary · `cond:trust`
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- FVAC-FHA/VA Amendatory Clause · `cond:fha-va`
- MLS AUC - Full Agent Report · req
- RCSD-B - Representative Capacity Signature · `cond:trust`
- RCSD-S - Representative Capacity Signature · `cond:trust`
- RLAS - Residential Lease After Sale (30 Days+) · `cond:seller-in-possession`
- SIP - Seller In Possession (Up to 29 Days) · `cond:seller-in-possession`
- SIPA - Seller In Possession Advisory · `cond:seller-in-possession`
- SPRP - Seller's Purchase of Replacement Property · `cond:replacement-property`
- Tax Record/Realist Tax · req
- TOPA - Tenant Occupied Property Addendum · `cond:tenant-occupied`
- Verification of Loan Application (Lender Pre) · req
- Verification of Funds (POF) · req
- Rejected Offers · *if applicable*
- Miscellaneous Sales Docs · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- AVID - Buying Agent Visual Inspection Disclosure · req
- AVID - Listing Agent Visual Inspection Disclosure · req
- APD - Amendment to Prior Disclosure · *if applicable*
- BHAA - Buyers HOA Advisory · `cond:hoa`
- COOP-OA -Stock Cooperative Ownership Advisory · `cond:coop`
- Environmental Hazards Handbook Receipt · req
- FHDS-Fire Hardening and Defensible Space Advisory · `cond:firezone` — HELP: (if in High Fire Zone)
- HID- For FHA/VA Loans · `cond:fha-va`
- Historical DIsclosures · *if applicable*
- KASE Disclosures · req
- Local County/City Disclosures · req
- LPD- Lead-Based Paint and Lead-Based Paint Hazard · `cond:pre1978`
- MCA - Market Conditions Advisory · req
- NHD Receipt · req
- PA- Probate Advisory · `cond:probate`
- PSD - Parking & Storage Disclosure (Condos Only) · `cond:condo`
- Residential Earthquake Hazard Report (Pre-1960) · `cond:pre1960` — Pre-1960
- SBSA - Statewide Buyer & Seller Advisory · req
- SFLS- Square Footage & Lot Size Disclosure · req
- SOLAR - Solar Questionnaire · `cond:solar`
- SPT- Notice of Supplemental Property Tax Bill · req
- SPQ - Seller Property Questionnaire · req
- TDS - Transfer Disclosure Statement · req
- ESD - Exempt Seller Disclosure · `cond:esd`
- TA - Trust Advisory · `cond:trust`
- TIC-OA -Tenancy In Common Ownership Advisory · `cond:tic`
- TIC-FD -Tenancy In Common Financial Disc Statement · `cond:tic`
- WBSA - Wooden Balcony and Stairs Addendum · *if applicable*
- WFDA - Wildfire Disaster Advisory · req
- WCMD - Water Conserving Plumbing & Carbon Mon · req
- WHSD - Water Heater Smoke Detector (if TDS Exempt) · `cond:esd` — If there is no TDS- Seller to provide WHS or WHSD
- Miscellaneous Disclosures · *if applicable*

**Reports**

- BIW - Buyer Inspection Waiver · `cond:inspection-waived`
- Home Inspection · *if applicable* — No asterisk on Sksylope
- NHD Report · req
- Preliminary Report · req
- Pool Inspection · *if applicable*
- Roof Inspection · *if applicable*
- Other Inspections · *if applicable*
- Septic Inspection · *if applicable*
- Sewer Lateral Inspection · *if applicable*
- Termite Inspection · *if applicable*
- Termite Clearance · *if applicable*
- Well Inspection · *if applicable*
- Asbestos Inspection · *if applicable*
- RR & RRRR - Request for Repairs/Response · *if applicable*
- RFR - Receipt for Reports · *if applicable*
- 9a Report (LA City) · `cond:la-city`
- COC - Certificate of Compliance (LA City) · `cond:la-city`

**Closing Documents**

- CDA Signed · req
- Closing Package · *if applicable*
- Buyer Signed Prelim Report Receipt from Escrow · req
- HOA Receipt from Escrow · `cond:hoa` — Skyslope: HOA Document Package *
- Final Closing Statement · req
- Home Warranty · req
- MLS Sold - Full Agent Report · req
- Completed FIRPTA with SSN or QS · req
- RFA - Referral Fee Agreement · `cond:referral`
- VP - Verification of Property Condition · req
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE Vacant Land Listing
`kase-vacant-land-listing` · 30 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and e-mail · *field*
- Preliminary Title Report · req
- Tax Record / Realist Report · req
- VLL - Vacant Land Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- AD - Agency Disclosure · req
- BCA - Buyer Compensation Advisory · req
- PRBS-S - Possible Rep More than one Buyer · req
- FHDA - Fair Housing Discrimination Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- KASE Listing ADM · req
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- Coming Soon Form (MLS) · `cond:coming-soon`
- DIA - Disclosure Information Advisory · req
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- MLS Active - Full Agent Report · req
- MT-LA - Modification of Listing Terms · *if applicable*
- RCSD - Representative Capacity Signature Disc · `cond:trust`
- Rejected Offers · *if applicable*
- RFR - Referral Fee Agreement · `cond:referral`
- SVLA - Sellers Vacant Land Advisory · req
- SELI - Exclude Listing from Internet · `cond:off-internet`
- TA - Trust Advisory · `cond:trust`
- Trust, Notarized Cert of Trust or Testamentary · `cond:trust` — Help Text: Testamentary only for Probate Listings
- Entity Docs (LLC or Corp) · `cond:trust`
- VLQ Seller Vacant Land Questionnaire Seller Signed · req
- Miscellaneous - Listing · *if applicable*
- COL - Cancellation of Listing · `cond:canceled`

## KASE Vacant Land Purchase
`kase-vacant-land-purchase` · 75 items

**Sales Documentation**

- Broker Notes · *field*
- TC For File - Please add your Name and email · *field*
- VLPA - Vacant Land Purchase Agreement · req
- SMCO - Seller Multiple Counter Offer · `cond:counter`
- SCO - Seller Counter Offer(s) · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Brokerage Acknowledgement · `cond:team`
- AC - Confirmation of Real Estate Agency · *if applicable*
- AD - Agency Disclosure · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AEA - Amendment of Existing Terms · *if applicable*
- Advisory Regarding Geographic Targeting Order · *if applicable*
- AOAA - Assignment of Agreement Addendum · *if applicable*
- BCA - Broker Compensation Advisory · req
- BRBC - Buyer Rep & Broker Compensation Agreement · req — HELP: Only upload if representing Buyer
- BVLIA - Buyers Vacant Land Additional Inspection · req
- CCPA - California Consumer Privacy Act Advisory · req
- COP - Contingency of Sale of Buyers Property · `cond:contingent-sale`
- CR - Inspection · req
- CR - Appraisal · req
- CR - Loan · req
- CR - Removal of ALL Contingencies · req
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- EMD RECEIPT · req
- Escrow Acknowledgement (page 17) · req
- Escrow Instructions · req
- Escrow Commission Instructions w/Broker Signature · req
- ETA - Extension of Time · *if applicable*
- FHDA- Fair Housing Discrimination Advisory · req
- FVAC-FHA/VA Amendatory Clause · `cond:fha-va`
- MLS AUC - Full Agent Report · req
- PRBS-B - Possible Rep More than one Buyer or Seller · req
- RCSD-B - Representative Capacity Signature · `cond:trust`
- RCSD-S - Representative Capacity Signature · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust` — HELP: only if representing Entity Buyer
- Trust, Notarized Certificate of Trust or Testamentary · `cond:trust` — HELP: only if representing Buyer Trustee
- Tax Record/Realist Tax · req
- Verification of Funds · req
- Verification of Loan Application · *if applicable*
- WFA - Wire Fraud Advisory · req
- Rejected Offers · *if applicable*
- Miscellaneous Sales Docs · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- Environmental Hazards Handbook Receipt · req
- Historical Disclosures · *if applicable*
- KASE Disclosures · req
- Local County / City Disclosures · *if applicable*
- MCA - Market Conditions Advisory · req
- NHD Receipt · req
- SBSA - Statewide Buyer & Seller Advisory · req
- SPT- Notice of Supplemental Property Tax Bill · req
- SFLS - Square Footage And Lot Size Disclosure · req
- TA - Trust Advisory · `cond:trust`
- VLQ - Seller Vacant Land Questionnaire · req
- WFDA -Wildfire Disaster Advisory · req
- Miscellaneous Disclosures · *if applicable*

**Reports**

- Preliminary Title Report · req
- NHD Report · req
- BIW - Buyer Inspection Waiver · `cond:inspection-waived`
- Environmental Report · *if applicable*
- RFR - Receipt for Reports · *if applicable*
- Septic Inspection · *if applicable*
- Soil Inspection Report · *if applicable*
- Well Inspection · *if applicable*
- Other Inspections · *if applicable*

**Closing Documents**

- Buyer Signed Prelim Report Receipt from Escrow · req
- CDA Signed · req
- Final Closing Statement · req
- MLS Sold - Full Agent Report · req
- Completed FIRPTA with SSN or QS · req
- RFA - Referral Fee Agreement · `cond:referral`
- W-9 (upload to commission tab) · `cond:referral`

## KASE Mobile Home Listing
`kase-mobile-home-listing` · 30 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and email · *field*
- Preliminary Title Search · *if applicable*
- Tax Record Printout / Realist Report · req
- RLA - Residential Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- NHD Report · req
- MHLA - Manufactured Home Listing Addendum · req
- KASE Listing ADM · req
- DIA - Disclosure Information Advisory · req
- AD - Agency Disclosure · req
- SA - Seller Advisory · req
- FHDA-Fair Housing Discrimination Advisory · req
- PRBS-S - Possible Rep More than on Buyer · req
- CCPA - California Consumer Privacy Act Advisory · req
- BCA - Buyer Compensation Advisory · req
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- MT-LA - Modification of Terms · *if applicable*
- Coming Soon Form (MLS) · `cond:coming-soon`
- MLS Active - Full Agent Report · req
- FHDS-Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD shows High Fire Zone
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- RCSD - Representative Capacity Signature Disc · `cond:trust`
- TA - Trust Advisory · `cond:trust`
- Trust, Notarized Cert of Trust or Testamentary · `cond:trust` — Help Text: Testamentary only for Probate Listings
- Entity Docs (LLC or Corp) · `cond:trust`
- RFA - Referral Fee Agreement · `cond:referral`
- Miscellaneous - Listing · *if applicable*
- COL - Cancellation of Listing · `cond:canceled`

## KASE Mobile Home Purchase
`kase-mobile-home-purchase` · 100 items

**Sales Documentation**

- BROKER NOTES · *field*
- TC for File - Please add your full name and email · *field*
- RPA - Residential Purchase Agreement · req
- SMCO - Seller Multiple Counter Offer · `cond:counter`
- SCO - Seller Counter Offer(s) · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- AC - Confirmation of Real Estate Agency · *if applicable*
- AD - Agency Disclosure · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AEA - Amendment of Exisiting Terms · *if applicable*
- AOAA - Assignment of Agreement Addendum · *if applicable*
- BIA - Buyers Inspection Advisory · req
- BCA - Broker Compensation Advisory · req
- BRBC - Buyer Representation & Broker Compensation · `side:buy` — HELP: Only upload if representing Buyer · There is no asterisk on Skyslope
- CBC - Cooperating Broker Compensation · *if applicable*
- CCPA - California Consumer Privacy Act Advisory · req
- Commission Instructions Signed · req
- COP - Contingency of Sale of Buyers Property · `cond:contingent-sale`
- CR - Inspection · req
- CR - Appraisal · req
- CR - Loan · req
- CR - Removal of ALL Contingencies · req
- Escrow Instructions · req
- EMD Receipt · req
- Escrow Acknowledgement (Page 17) · req
- ETA - Extension of Time Addendum · *if applicable*
- FHDA - Fair Housing Discrimination Advisory · req
- FVAC - FHA/VA Amendatory Clause · `cond:fha-va`
- MHDA - Manufactured Home Dealer Addendum · *if applicable*
- MH- PA Manufactured or Mobile Home Purchase Adm · req
- MLS AUC - Full Agent Report · req
- Park Approval · req
- PRBS-B - Possible Rep More than one Buyer or Seller · req
- RCSD-B - Representative Capacity Signature · `cond:trust`
- RCSD-S - Representative Capacity Signature · `cond:trust`
- RLAS - Residential Lease After Sale (30 Days+) · `cond:seller-in-possession`
- SIP - Seller In Possession (Up to 29 Days) · `cond:seller-in-possession`
- Tax Record / Realist Tax · req
- TOPA - Tenant Occupied Property Addendum · `cond:tenant-occupied`
- WFA - Wire Fraud Advisory · req
- Verification of Loan Application · req
- Verifcation of Funds · req
- Entity Docs (LLC or Corp) · `cond:trust` — HELP: (only if representing Entity Buyer)
- Trust, Notarized Certificate of Trust or Testamentary · `cond:trust` — HELP: (only if representing Buyer Trustee)
- Miscellaneous Sales Docs · *if applicable*
- Rejected Offers · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- AVID - Listing Agent Visual Inspection Disclosure · req
- AVID - Buying Agent Visual Inspection Disclosure · req
- BHAA - Buyers HOA Advisory · `cond:hoa`
- Environmental Hazards Handbook Receipt · req
- ESD - Exempt Seller Disclosure · `cond:esd`
- FHDS-Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD shows High Fire Zone
- Historical Disclosures · *if applicable* — Is this required for mobile homes?
- Local County / City Disclosures · req
- KASE Disclosures · req
- LPD - Lead-Based Paint and Lead-Based Paint Hazard · `cond:pre1978`
- MCA - Market Conditions Advisory · req
- MHTDS - Mobile Home Transfer Disclosure Statement · req
- NHD Receipt · req
- PSD - Parking & Storage Disclosure · `cond:condo`
- Residential Earthquake Hazard Report (Pre-1960) · `cond:pre1960` — Pre-1960
- SBSA - Statewide Buyer & Seller Advisory · req
- SFLS - Square Footage and Lot Size Disclosures · req
- SPT - Notice of Supplemental Property Tax Bill · req
- SPQ - Seller Property Questionnaire · req
- TDS - Transfer Disclosure Statement · req
- TA - Trust Advisory · `cond:trust`
- WCMD - Water Conserving Plumbing & Carbon · req
- WHSD - Water Heater Smoke Detector (if TDS Exempt) · `cond:esd` — If there is no TDS- Seller to provide WHS or WHSD
- WFDA - Wildfire Disaster Advisory · req
- Miscellaneous Disclosures · *if applicable*

**Reports**

- Preliminary Title Search (HCD) · req
- NHD Report · req
- BIW - Buyer Inspection Waiver · `cond:inspection-waived`
- Home Inspection · req
- Pool Inspection · *if applicable*
- Roof Inspection · *if applicable*
- Septic Inspection · *if applicable*
- Sewer Lateral Inspection · *if applicable*
- Termite Inspection · *if applicable*
- Termite Clearance · *if applicable*
- Well Inspection · *if applicable*
- Other Inspections · *if applicable*
- RFR - Receipt for Reports · req
- RR & RRRR - Request for Repairs/Response · *if applicable*
- CLOSING DOCUMENTATION · req

**Closing Documents**

- Buyer Signed Prelim from Escrow · req
- HOA Receipt from Escrow · req
- CDA Signed · req
- Final Closing Statement · req
- MLS Sold - Full Agent Report · req
- Completed FIRPTA with SSN or QS · req
- VP - Verification of Property · req
- RFA - Referral Agreement · `cond:referral`
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE Lease Listing
`kase-lease-listing` · 28 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and e-mail · *field*
- Tax Record Printout / Realist Report · req
- LL - Lease Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- AD - Agency Disclosure · req
- Addendum to the Lease Listing Agreement · *if applicable*
- BBD - Bed Bug Disclosure · req
- CCPA - California Consumer Privacy Act Advisory · req
- Coming Soon Form (MLS) · `cond:coming-soon`
- FHDA - Fair Housing Discrimination Advisory · req
- KASE ESA - Electronic Signature Addendum · req
- KLA - Keysafe / Lockbox Addendum · *if applicable*
- LPD - Lead Base Paint Disclosure · `cond:pre1978`
- MLS Active - Full Agent Report · req
- RCJC - Rent Cap & Just Cause Addendum · req
- TFHD - Tenant Flood Hazard Disclosure · req
- TRPR - Tenant Positive Rental Reporting · req
- RPOA - Rental Property Owner Advisory · req
- RPOD- Rental Property Owner Disclosure · req
- SDDA - Security Deposit Disclosure and Addendum · *if applicable*
- WSM - Water Submeter Addendum · req
- RCSD-LL - Representative Capacity Signature · `cond:trust`
- MT-LA - Modification of Terms of Listing Agreement · *if applicable*
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- Entity Docs (LLC or Corp) · `cond:trust`
- Miscellaneous - Listing · *if applicable*
- COL - Cancellation of Listing · `cond:canceled`

## KASE Lease Tenant
`kase-lease-tenant` · 41 items

**Sales Documentation**

- Broker Notes · *field*
- TC For File - Please add your Name in Text Box · *field*
- TRBC - Tenant Rep & Broker Compensation Agreement · req
- RENT SPREE Application · req
- LRA - Application to Rent/ Screening Fee · *if applicable*
- AD - Agency Disclosure · req
- CCPA - California Consumer Privacy Act Advisory · req
- FHDA - Fair Housing Discrimination Advisory · req
- LR - Residential Lease or Month to Month Rental · req
- MII- Move In Insp. Follow up 3 days from delivery. · req
- Tax Record Printout · req
- MLS AUC - Agent Full Detail Report · req
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- KASE ESA - Electronic Signature Addendum · req
- CLR - Cancellation of Lease Rental · `cond:canceled`

**Disclosures**

- BBD - Bed Bug Disclosure · req
- ATCA - Animal Terms Conditions Addendum · *if applicable*
- Environmental Hazards Handbook Receipt · req
- LPD - Lead Based Paint Disclsoure · `cond:pre1978`
- LRM - Lease Rental Mold Addendum · req
- MCN - Methamphetamine Contamination Notice · *if applicable*
- PHSA - Pool / Hot Tub & SPA Addendum · *if applicable*
- PSD - Parking & Strorage Disclosure · `cond:condo`
- RCJC - Rent Cap & Just Cause Addendum · req
- RCSD-LL - Representative Capacity Signature · `cond:trust`
- RCSD-T - Representative Capacity Signature · `cond:trust`
- RPOD- Rental Property Owner Disclosure · req
- SSDA - Security Deposit Disclosure and Addendum · *if applicable*
- TFHD - Tenant Flood Hazard Disclosure · req
- TRPR - Tenant Rental Payment ReportIng · req
- WCMD - Water Conserving/Carbon Monoxide · req
- WHSD - Water Heater/Smoke Detector · req
- WSM - Water Submeter Addendum · *if applicable*
- Miscellaneous - Disclosures · *if applicable*

**Closing Documents**

- CDA - Signed · req
- Check & Relevant Docs · req
- Lease invoice · req
- MLS Sold - Full Agent Report · req
- Proof of Liability Insurance (if 30C is checked) · *if applicable* — If item 30C on RLMM is checked
- Referral Agreement · `cond:referral`
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE Commercial List
`kase-commercial-list` · 30 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and e-mail · *field*
- Preliminary Title Report · req
- Tax Record / Realist Report · req
- CLA - Commercial & Residential Income Listing · req
- MLSA - Multiple Listing Service Addendum · req
- NHD Report · req
- AD - Agency Disclosure · req
- FHDA - Fair Housing Discrimination Advisory · req
- PRBS-S - Possible Rep More than one Buyer · req
- SA - Sellers Advisory · req
- BCA - Buyer Compensation Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- MLS Active - Full Agent Report · req
- ABA - Additional Broker Acknowledgement · `cond:team`
- AAA - Additional Agent Acknowledgement · `cond:team`
- Coming Soon Form (MLS) · `cond:coming-soon`
- DIA - Disclosure Information Advisory · req
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- KLA - Keysafe / Lockbox Addendum · *if applicable*
- MT-LA - Modification of Terms of Listing Agreement · *if applicable*
- FHDS-Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD shows High Fire Zone
- NSE - Notice of Sale & Entry · *if applicable*
- RCSD-S - Representative Capacity Signature Dis · `cond:trust`
- TA - Trust Advisory · `cond:trust`
- Trust, Notarized Certificate of Trust or Testament · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust`
- RFA - Referral Fee Agreement · `cond:referral`
- Miscellaneous - Listing · *if applicable*
- COL - Cancelation of Listing · `cond:canceled`

## KASE Commercial Purchase
`kase-commercial-purchase` · 99 items

**Sales Documentation**

- Broker Notes · *field*
- TC for File - Please add your name and email · *field*
- RIPA - Residential Income Purchase Agreement · req
- SMCO - Seller Multiple Counter Offer · `cond:counter`
- SCO - Seller Counter Offer(s) · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- AC - Confirmation of Real Estate Agency · *if applicable*
- AD - Agency Disclosure · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AEA - Amendment of Existing Terms · *if applicable*
- AOAA - Assignment of Agreement Addendum · *if applicable*
- BCA - Broker Compensation Advisory · req
- BIA - Buyers Rep & Broker Compensation Agreement · req
- BRBC - Buyer Rep & Broker Compensation Agreement · `side:buy`
- CCPA - California Consumer Privacy Act Advisory · req
- COP - Contingency of Sale of Buyers Property · `cond:contingent-sale`
- CR - Inspection · req
- CR - Appraisal · req
- CR - Loan · req
- CR - Removal of ALL Contingencies · req
- APPROVAL of LESS THAN 2% COMMISSION · `cond:low-commission`
- Escrow Acknowledgement (Page 17) · req
- EMD - Earnest Money Deposit · req
- Escrow Instructions · req
- Escrow Commission Instructions w/Broker Signature · req
- ETA - Extension of Time Amendment · *if applicable*
- FHDA - Fair Housing Discriminatory Advisory · req
- FVAC-FHA/VA Amendatory Clause · `cond:fha-va`
- Lease Agreement · *if applicable*
- MLS AUC - Full Agent Report · req
- PRBS-B - Possible Rep More than one Buyer or Seller · req
- RCSD-B - Representative Capacity Signature · `cond:trust`
- RCSD-S - Representative Capacity Signature · `cond:trust`
- RLAS - Residential Lease After Sale (30 Days+) · `cond:seller-in-possession`
- SIP - Seller In Possession (Up to 29 Days) · `cond:seller-in-possession`
- Tax Record/Realist Tax · req
- TOPA - Tenant Occupied Property Addendum · `cond:tenant-occupied`
- Verification of Funds · req
- Verification of Loan Application · req
- WFA - Wire Fraud Advisory · req
- Entity Docs (LLC or Corp) · `cond:trust`
- Trust, Notarized Certificate of Trust · `cond:trust`
- Rejected Offers · *if applicable*
- Miscellaneous Sales Doc · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- AVID - Buying Agent Visual Inspection Disclosure · *if applicable* — Only for 4 units or less.
- AVID - Listing Agent Visual Inspection Disclosure · req
- Environmental Hazards Handbook Receipt · req
- ESD - Exempt Seller Disclosure · `cond:esd` — Only for probate or REO
- FHDS - Fire Hardening and Definsible Space Advisory · `cond:firezone` — Only applicable if in high fire zone.
- Historical Disclosures · *if applicable*
- Income & Expense Statement · *if applicable*
- KASE Disclosures · req
- Local County/City Disclosures · req
- LPD - Lead-Based Paint and Lead-Based Paint Hazard · `cond:pre1978`
- MCA - Market Conditions Advisrory · req
- NHD Receipt · req
- Propane Tank Addendum · *if applicable* — Remove "Side Form"
- Residential Earthquake Hazard Report (Pre-1960) · `cond:pre1960` — Pre-1960
- SBSA - Statewide Buyer & Seller Advisory · req
- SFLS - Square Footage & Lot Size Disc & Advisroy · req
- SPT - Notice of Supplemental Property Tax Bill · req
- CSPQ - Seller Property Questionnaire · req
- TA - Trust Advisory · `cond:trust`
- TEC - Tenant Estoppel Certificate(s) · *if applicable*
- Unit Rental Agreement(s) / Lease(s) · *if applicable*
- WCMD - Water Conserving Plumbing & Carbon Mon · req
- WFDA - Wildfire Disaster Advisory · req
- WHSD - Water Heater Smoke Detector (if TDS Exempt) · `cond:esd` — If there is no TDS- Seller to provide WHS or WHSD
- Miscellaneous Disclosures · *if applicable*

**Reports**

- Preliminary Report · req
- NHD Report · req
- BIW - Buyer Inspection Waiver · req
- Home Inspection · req
- Asbestos Inspection · *if applicable*
- Pool Inspection · *if applicable*
- Roof Inspection · *if applicable*
- Septic Inspection · *if applicable*
- Sewer Lateral Inspection · *if applicable*
- Termite Inspection · *if applicable*
- Termite Clearance · *if applicable*
- Well Inspection · *if applicable*
- Other inspections · *if applicable*
- RFR - Receipt for Reports · *if applicable* — Remove "Buyer rep only"
- RR & RRRR - Request for Repairs / Response to RR · *if applicable*

**Closing Documents**

- Buyer Signed Prelim Report Receipt from Escrow · req
- CDA - Signed · req
- Closing Package · *if applicable*
- Home Warranty · req
- Final Closing Statement · req
- MLS Sold - Full Agent Report · req
- RFA - Referral Fee Agreement · `cond:referral`
- Completed FIRPTA with SSN or QS · req
- VP - Verification of Property · req
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE Commercial & Residential Income Listing (5+ UNITS)
`kase-commercial-residential-income-listing-5-units` · 36 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and e-mail · *field*
- Preliminary Title Report · req
- Tax Record / Realist Report · req
- CLA - Commercial & Residential Income Listing · req
- MLSA - Multiple Listing Service Addendum · req
- NHD Report · req
- AD - Agency Disclosure · req
- KASE Listing ADM · req
- Estoppel Certificate · req
- Environmental Report · *if applicable* — Help Text: If Industrial
- FHDA - Fair Housing Discrimination Advisory · req
- PRBS-S - Possible Rep More than one Buyer · req
- SA - Sellers Advisory · req
- BCA - Buyer Compensation Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- MLS Active - Full Agent Report · req
- CSPQ - Commercial Seller Property Questionnaire · req
- Commercial Property Guide to Earthquake Safety · req
- ABA - Additional Broker Acknowledgement · `cond:team`
- AAA - Additional Agent Acknowledgement · `cond:team`
- Coming Soon Form (MLS) · `cond:coming-soon`
- DIA - Disclosure Information Advisory · req
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- KLA - Keysafe / Lockbox Addendum · *if applicable*
- MT-LA - Modification of Terms of Listing Agreement · *if applicable*
- FHDS-Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD shows High Fire Zone
- NSE - Notice of Sale & Entry · *if applicable*
- RCSD-S - Representative Capacity Signature Dis · `cond:trust`
- Rent Roll or Lease Agreement · req
- TA - Trust Advisory · `cond:trust`
- Trust, Notarized Certificate of Trust or Testament · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust`
- RFA - Referral Fee Agreement · `cond:referral`
- Miscellaneous - Listing · *if applicable*
- COL - Cancelation of Listing · `cond:canceled`

## KASE Commercial & Residential Income Purchase (5+ UNITS)
`kase-commercial-residential-income-purchase-5-units` · 75 items

**Sales Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and e-mail · *field*
- Tax Record / Realist Report · req
- CPA - Commercial Property Purchase Agreement · req
- SCO - Seller Counter Offer(s) · `cond:counter`
- SMCO - Seller Multiple Counter Offer · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- AC - Agency Confirmation · *if applicable*
- AD - Agency Disclosure · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AEA - Amendment of Existing Terms · *if applicable*
- AOAA - Assignment of Agreement Addendum · *if applicable*
- BCA - Buyer Compensation Advisory · req
- BIA - Buyer's Investigation Advisory · req
- BHIA - Buyer Homeowners Insurance Advisory · req
- BRBC - Buyer Rep & Broker Compensation Agreement · `side:buy` — *If we rep buyer only.
- CR - Inspection · req
- CR - Appraisal · req
- CR - Loan · req
- CR - Removal of ALL Contingencies · req
- APPROVAL of LESS THAN 2% COMMISSION · `cond:low-commission`
- Escrow Acknowledgement (Page 17) · req
- EMD - Earnest Money Deposit · req
- Escrow Instructions · req
- Escrow Commission Instructions w/Broker Signature · req
- ETA - Extension of Time Amendment · *if applicable*
- Lease Agreement · *if applicable*
- MLS AUC - Full Agent Report · req
- PRBS-B - Possible Rep More than one Buyer · req
- RCSD-B - Representative Capacity Signature Dis · `cond:trust`
- RCSD-S - Representative Capacity Signature Dis · `cond:trust`
- SIP - Seller in Possession (Up to 29 Days) · `cond:seller-in-possession`
- TOPA - Tenant Occupied Property Addendum · `cond:tenant-occupied`
- Verification of Funds · req
- Verification of Loan Application · req
- WFA - Wire Fraud Advisory · req
- Entity Docs (LLC or Corp) · `cond:trust`
- Rejected Offers · *if applicable*
- Miscellanious Sales Docs · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- Environmental Hazards Handbook Receipt · req
- ESD - Exempt Seller Dislcosures · `cond:esd`
- CSP - Commercial Seller Property Questionnaire · req
- TEC - Tenant Estoppel Certificate(s) · req
- Rent Roll · req
- Income and Expenses · req
- Rental and Service Agreements · *if applicable*
- KASE Disclosures · req
- Local County / City Disclosures · req
- LPD - Lead-Based Paint and Lead-Based Paint Hazard · `cond:pre1978` — Pre-1978
- NHD Receipt · req
- EDUBA - Energy Use Disclosure and Benchmarking Advisory · req
- Miscellanious Disclosures · *if applicable*

**Reports**

- Preliminary Title Report · req
- NHD Report · req
- Environmental Report · *if applicable* — Help Text: If Industrial
- Inspections · req
- BIW - Buyer Inspection Waiver · `cond:inspection-waived`
- RFR - Receipt for Reports · *if applicable*
- RR & RRRR - Request for Repairs / Response to RR · *if applicable*
- ESA - Phase 1 Environamental Site Assessment · req
- ESA - Phase 2 Environamental Site Assessment · req

**Closing Documents**

- Buyer Signed Prelim Receipt from Escrow · req
- CDA Signed · req
- Closing Package · *if applicable*
- Final Closing Statement · req
- MLS Sold - Full Agent Report · req
- RFA - Referral Agreement Fee · `cond:referral`
- Completed FIRPTA with SSN or QS · req
- VP - Verification of Property · req
- W-9 Other Broker (upload To commission tab) · `cond:referral`

## Kase New Construction Listing
`kase-new-construction-listing` · 34 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and email · *field*
- Preliminary Title Report · req
- Tax Record / Realist Report · req
- RLA - Residential Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- NHD REPORT · req
- KASE Listing ADM · req
- AD - Agency Disclosure · req
- SA - Seller Advisory · req
- BCA - Buyer Compensation Advisory · req
- PRBS-S - Possible Rep of More than one Buyer or Sell · req
- FHDA - Fair Housing Discrimination Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- AAA - Additional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- Coming Soon Form (MLS) · `cond:coming-soon`
- MLS Active - Full Agent Report · req
- DIA - Disclosure Information Advisory · req
- MT-LA - Modification of Terms Listing Agreement · *if applicable*
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- TA - Trust Advisory · `cond:trust`
- RCSD-S- Representative Capacity Signature Disclos · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust`
- RFA - Referral Fee Agreement · `cond:referral`
- FHDS - Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD Report shows High Fire Zone
- TDS- Seller Signed · req
- SPQ- Seller Signed · req
- AVID- Seller/Listing Agent Signed · req
- NCA - New Construction Advisory · req
- NCNC - Notice of Completion & to Close Escrow · req
- NC Sub Termite Soil Treatment Record (FHA & VA) · *if applicable* — New Construction Subterranean Termite Soil Treatment Records (FHA & VA Offers) *
- Miscellaneous - Listing · *if applicable*
- COL - Cancellation of Listing · `cond:canceled`

## KASE New Construction Purchase
`kase-new-construction-purchase` · 73 items

**Sales Documentation**

- BROKER NOTES · *field*
- TC for File - Please add your name and email · *field*
- NCPA - New Construction Purchase or Sellers Agreement · req
- SMCO - Seller Multiple Counter Offer · `cond:counter`
- SCO - Seller Counter Offer(s) · `cond:counter`
- BCO - Buyer Counter Offer(s) · `cond:counter`
- AD - Agency Disclosure · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- AAA - Addtional Agent Acknowledgement · `cond:team`
- ABA - Additional Broker Acknowledgement · `cond:team`
- AEA - Amendment of Existing Terms · *if applicable*
- BCA - Broker Compensation Advisory · req
- BIA - Buyers Inspection Advisory · req
- BRBC - Buyer Rep & Broker Compensation Agreement · `side:buy` — Only needed if representing Buyer.
- CCPA - California Consumer Privacy Act Advisory · req
- NCEI - Common Int Subdiv Supp Escrow Inst Add · *if applicable*
- COP - Contingency of Sale of Property · `cond:contingent-sale`
- CR - Contingency Removal #1 · req — There's an asterisk on Skylope
- CR - Contingency Removal #2 · *if applicable*
- CR - Contingency Removal #3 · *if applicable*
- Escrow Instructions · req
- ETA - Extension of Time Addendum · *if applicable*
- FHDA - Fair Housing Discrimination Advisory · req
- FVAC-FHA/VA Amendatory Clause · `cond:fha-va`
- MLS AUC - Full Agent Report · req
- NCA - New Construction Advisory · req
- NCA - New Construction Options and Upgrades Addendum · *if applicable*
- NCRPA - New Construction Addendum to RPA · *if applicable*
- NCNC - Notice of Completion & to Close Escrow · *if applicable*
- NBP or NSP - Notice to Perform · *if applicable*
- PRBS-B - Poss Rep of More Than One Buyer or Seller · req
- Receipt for Increased Deposit (from Escrow) · *if applicable*
- RCSD-S - Representative Capacity Signature Disc · `cond:trust`
- RCSD-B - Representative Capacity Signature Disc · `cond:trust`
- Tax Record/ Realist Tax · req
- Entity Docs (LLC or Corp) · `cond:trust`
- WFA - Wire Fraud Advisory · req
- Miscellaneous (add name in desc box) · *if applicable*
- CC - Cancellation of Contract · `cond:canceled`

**Disclosures**

- BHAA - Buyers HOA Advisory · `cond:hoa`
- CFCO - Cert of Final Completion & Occupancy · *if applicable*
- City Specific Requirements/Disclosures · req — There's an asterisk on Skylsope
- Developers Disclosure · *if applicable*
- LA AVID - Agent Visual Inspection Disclosure · req
- SA AVID - Agent Visual Inspection Disclosure · req
- Local Gen Info / Disclosure & Disclaimer · *if applicable*
- MCA - Market Conditions Advisory · req
- NHD Receipt · req

**Listing Documentation**

- FHDS - Fire Hardening and Defensible Space Advisory · `cond:firezone` — Help Text: If NHD Report shows High Fire Zone

**Disclosures**

- Receipt for Public Report · *if applicable*
- Receipt for Residential Environmental Booklet · req
- SPQ - Seller Property Questionnaire · req
- SFLS - Square Footage and Lot Size Advisory · req
- SBSA - Statewide Buyer & Seller Advisory · req
- TDS - Transfer Disclsoure Statement · req
- VP - Verification of Property Condition · req
- WCMD - Water Conserving Monoxide Detector Notice · req
- WHSD - Water Heater Smoke Detector (TDS Exempt) · req — If there is no TDS- Seller to provide WHS or WHSD

**Reports**

- Home Inspection · req
- NHD Report · req
- Preliminary Title Report · req
- Public Report · req

**Closing Documents**

- CDA - Signed · req
- HOA Receipt from Escrow · `cond:hoa`
- Buyer Signed Prelim Receipt from Escrow · req
- Check & Relevant Docs · req
- Final Closing Statement · req
- Completed FIRPTA with SSN or QS · req
- MLS Closed - Full Agent Report · req
- RFA - Referral Fee Agreement · req
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE Commercial Lease Listing
`kase-commercial-lease-listing` · 15 items

**Listing Documentation**

- BROKER NOTES · *field*
- TC For File - Please add your Name and email · *field*
- Tax Record /Realist Tax · req
- Commercial Lease Listing Agreement · req
- MLSA - Multiple Listing Service Addendum · req
- AD - Agency Disclosure · req
- BCA - Broker Compensation Advisory · req
- CCPA - California Consumer Privacy Act Advisory · req
- FHDA - Fair Housing Discrimination Advisory · req
- PRBS-S - Possible Rep of More than one Buyer or Sell · req
- RPOD- Rental Property Owner Disclosure · req
- Miscellaneous · *if applicable*
- MT-LA - Modification of Terms · *if applicable*
- APPROVAL of LESS THAN 2% commission · `cond:low-commission`
- COL - Cancellation of Listing · req

## KASE Commercial Lease Tenant
`kase-commercial-lease-tenant` · 29 items

**Sales Documentation**

- BROKER NOTES · *field*
- TC for File - Please add your name and email · *field*
- AD - Agency Disclosure · req
- BCA - Buyer Compensation Advisory · req
- BRBC - Buyer Representation & Broker Compensation · req
- CL - Commercial Lease Agreement · req
- RentSpree or Application to Rent · req
- MLS AUC - Agent Full Detail Report · req
- ADM - Addendum #1 · *if applicable*
- ADM - Addendum #2 · *if applicable*
- ADM - Addendum #3 · *if applicable*
- APPROVAL of LESS THAN 2% COMMISSION · `cond:low-commission`
- RCSD-T - Representative Capacity Signature · `cond:trust`
- RCSD-LL - Representative Capacity Signature · `cond:trust`
- Entity Docs (LLC or Corp) · `cond:trust`
- Tax Record/Realist Tax · req
- Verification of Funds · *if applicable*
- Miscellaneous · *if applicable*
- Cancellation Of Contract · `cond:canceled`

**Disclosures**

- WCMC - Water Conserving · req — Help text: Water Conserving ONLY
- WHSD - Water Heater/Smoke Detector · req
- Miscellaneous Disclosures · *if applicable*

**Closing Documents**

- CDA - Signed · req
- Check & Relevant Docs · req
- Lease Invoice · req
- MLS Printout - CLOSED · req
- Proof of Liability Insurance (see item 30 in CL) · *if applicable* — If item 30 on CL is completed.
- Referral Agreement · `cond:referral`
- W-9 for Other Broker (upload to commission tab) · `cond:referral`

## KASE New Construction - Buyer Referral
`kase-new-construction-buyer-referral` · 10 items

**Sales Documentation**

- BROKER NOTES · *field*
- BRBC - Buyer Representation/Broker Compensation (Buyer Rep Only) · `side:buy` — On Skyslope it says: BRBC- Buyer Representation/Broker Compensation · no asterisk on skyslope
- Builder Referral Agreement · req
- Commission Agreement · req
- Miscellaneous(1) - Sales · *if applicable*

**Closing Documents**

- CDA - Signed · req
- Check & Relevant Docs · req
- Closing Package · req
- Final Closing Statement · req
- Miscellaneous(1) - Closing · *if applicable*

## KASE Referral
`kase-referral` · 6 items

**Sales Documentation**

- BROKER NOTES · *field* — There's an asterisk on Skyslope

**Closing Documents**

- CDA - Signed · req
- Check & Relevant Docs · req
- RFA - Referral Fee Agreement · `cond:referral`
- Outgoing Referral Closing Statement · req
- W-9 from other Broker (upload to commission tab) · `cond:referral`
