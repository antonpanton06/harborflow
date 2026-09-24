#BUSINESS OUTCOME Keep the dispatch desk operational when a user enters a value outside the agreed range.
#Add validation loops for the cases below. After an error, repeat only the affected prompt.
#This compulsory task focuses on invalid values and formats and must be integrated across
#the product.
#• Menu: accept only integers 1-8.
#• Quote: distance and weight must be greater than zero; service code must be S, X or P.
#• Capacity: capacity and every parcel weight must be greater than zero.
#• Performance: promised and actual minutes cannot be negative; damaged parcels cannot be negative.
#• Weekly report: exactly seven non-negative delivery counts are required; target must be non-negative.
distance >= 0
weight >= 0 
capacity >= 0 
parcelWeights >=0


#Required error templates
#Error - Select a service from 1 to 8.
#Error - Value must be greater than zero.
#Error - Service code must be S, X or P.
#Error - Weekly report requires 7 delivery counts.
#The program must not crash, silently replace an invalid value, or return to the main menu before valid input has been collected.