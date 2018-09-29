# UK Postcodes Validation

The format is as follows, where  **A**  signifies a letter and  **9**  a digit:

| **Format** | **Coverage** | **Example** |
| --- | --- | --- |
| **AA9A 9AA** | WC postcode area; EC1–EC4, NW1W, SE1P, SW1 | EC1A 1BB |
| **A9A 9AA** | E1W, N1C, N1P | W1A 0AX |
| **A9 9AA** | B, E, G, L, M, N, S, W | M1 1AE |
| **A99 9AA** | B33 8TH |
| **AA9 9AA** | All other postcodes | CR2 6XH |
| **AA99 9AA** | DN55 1PT |

Notes:

- As all formats end with 9AA, the first part of a postcode can easily be extracted by ignoring the last three characters
- Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC is always subdivided by a further letter, e.g. WC1A).
- Areas with only double-digit districts: AB, LL, SO.
- Areas with a district &#39;0&#39; (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10).
- The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
- The letters _QVX_ are not used in the first position.
- The letters _IJZ_ are not used in the second position.
- The only letters to appear in the third position are _ABCDEFGHJKPSTUW_ when the structure starts with A9A.
- The only letters to appear in the fourth position are _ABEHMNPRVWXY_ when the structure starts with AA9A.
- The final two letters do not use the letters _CIKMOV_, so as not to resemble digits or each other when hand-written.
- Post code sectors are one of ten digits: 0 to 9 with 0 only used once 9 has been used in a post town, save for Croydon and Newport (see above).

A postcode can be validated against a table of all 1.7 million postcodes in [Code-Point Open](https://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html). The full delivery address including postcode can be validated against the Royal Mail Postcode Address File (PAF) which lists 29 million valid delivery addresses, constituting most (but not all) addresses in the UK.