def createTripPrompt(prompt_inputs):
    prompt = f"""Imagine you are a travel guide. You have been tasked with suggesting a trip plan for a group of people. The group will 
tell you their preferences and constraints and you will suggest a trip itinerary for them. The format of this itinerary is shared 
after the details given by the group.

Start Location: {prompt_inputs['start_location']}
Destination: {prompt_inputs['destination']}
Budget: {prompt_inputs['budget']}
Start Date: {prompt_inputs['start_date']}
End Date: {prompt_inputs['end_date']}
Mode of Arrival: {prompt_inputs['mode_of_arrival']}
Stay Preference: {prompt_inputs['stay_preference']}
Activity Preference: {prompt_inputs['activity_preference']}
Group Size: {prompt_inputs['group_size']}
Mode of Transport: {prompt_inputs['mode_of_transport']}

Mode of arrival is how the group will reach the destination and mode of transport is how the group plans on travelling around the
destination. Stay preference is the type of accommodation the group prefers and activity preference is the type of activities the group
wants to do while on the trip. The group size is the number of people in the group. The budget is the maximum amount of money the group
can spend including travel, accommodation, and activities.

The format of the itinerary is as follows:

1. Basic Information: Such as where the trip is to, the dates, and the group size.
2. Travel Information: Such as how the group will reach the destination and how the group will travel around the destination. Suggest 
alternative travel options if possible and if the chosen ones are not available or not ideal. 
3. Accommodation Information: Such as where the group will stay. Include multiple options if possible.
4. Activity Information: Such as what the group can do at the destination. Include multiple options if possible. The activites should be 
specific to the group's preferences and constraints. They should also align with their chosen activity preference.
5. Budget Information: Such as the cost of the trip and how the group can save money. Include tips on how to save money on travel, food,
activities and accomodation. Also include an estimated breakdown of the costs of the trip.
6. Safety Information: Such as the safety of the destination and how the group can stay safe. Include information on what to do in case 
of an emergency and how to get help.
7. Important Documents: Such as what documents the group needs to carry and where they can be required.
8. Timeline: Generate a rough timeline of each day of the trip. Include the time of each activity and the time of travel between places 
along with estimated costs.
"""
    return prompt


def createItineraryPrompt(prompt_inputs):
    prompt = f"""Imagine you are a travel guide. You have been tasked with creating an itinerary for a trip that has already been planned.
You are not supposed to suggest any changes to the trip plan. You are only supposed to create an itinerary for the trip. The format of
this itinerary is shared after the details given by the group.

Start Location: {prompt_inputs['start_location']}
Destination: {prompt_inputs['destination']}
Budget: {prompt_inputs['budget']}
Start Date: {prompt_inputs['start_date']}
End Date: {prompt_inputs['end_date']}
Group Size: {prompt_inputs['group_size']}
Mode of Arrival: {prompt_inputs['mode_of_arrival']}
Mode of Transport: {prompt_inputs['mode_of_transport']}
Accommodation: {prompt_inputs['accommodation']}
Activities: {prompt_inputs['activities']}
Extra Information: {prompt_inputs['extra_info']}

Mode of arrival is how the group will reach the destination and mode of transport is how the group plans on travelling around the
destination. The accomodation is where the group will stay. The activities are what the group will do at the destination. The extra
information is any additional information the group wants to share.

The format of the itinerary is as follows:

1. Basic Information: Start Location, destination, budget, start date, end date, group size
2. Travel Information: Mode of arrival and mode of transport with potential cost
3. Accommodation Information: Accommodation plans and potential cost
4. Activity Information: Activities planned and potential cost
5. Extra Information: Extra information
6. Important Documents: What documents the group needs to carry and where they can be required.
7. Timeline: Generate a rough timeline of each day of the trip. Include the time of each activity and the time of travel between places along
with estimated costs.
"""
    return prompt


def getHermesAIResponse(prompt):
    return "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."