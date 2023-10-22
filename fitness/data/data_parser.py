import json

mongodb_postgresql_exercises_map = {
    "64ea4ed0d051a16d1587f458": "e0b662a7-3801-480f-950e-17fd96badd13",
    "64ea5134d051a16d1587f4b5": "0ae8d7c4-6785-4fa9-9a6b-b60f657a0eab",
    "64ea5249d051a16d1587f511": "22c41f6a-69a0-432e-9cb6-ec8ec20d1049",
    "64cd57766ab6c2c899d1ff21": "fcae1fd6-d15c-4c38-b559-e1253775a05b",
    "64ea67f8d051a16d1587f531": "a33ebc0f-26fb-4031-ab40-268e62e27cb9",
    "64cd5a236ab6c2c899d1ff73": "51e2b73d-b2db-40a0-98cf-bd2fe0f5c038",
    "64cd58f46ab6c2c899d1ff4d": "7a0f6e96-57b7-40b6-b27f-4e3f088c47ca",
    "64ea51aed051a16d1587f4e3": "69949b6e-5f5b-4c55-9517-38720807b747",
    "64ea6d06d051a16d1587f5eb": "ed22b807-8824-44f4-986b-138366134322",
    "64cd5b0f6ab6c2c899d1ff89": "4042036c-f5be-43a0-8bb5-281baeef3576",
    "64ea6a60d051a16d1587f585": "6fd8a488-76d5-49c3-b6d5-6f072d07b287",
    "64cd4e686ab6c2c899d1fde0": "631cec69-e127-4049-839c-3b24b5924a55",
    "64ea6d5ed051a16d1587f5fb": "323efdd9-2c39-4dfa-9de1-24a836b6b82b",
    "64cd5c5d6ab6c2c899d1ffbb": "99e68eff-4116-4894-8a51-70e49404fff7",
    "64ea50a7d051a16d1587f4a5": "16e47117-87f2-4305-9de8-f31bc83765d7",
    "64ea4fb3d051a16d1587f48f": "059383f4-6e2b-4d9f-90f2-bb17781fa2a4",
    "64ea6b30d051a16d1587f5cb": "c28a23d6-18ef-4bec-99b9-3020b2b430e5",
    "64ea90aad051a16d1587fde0": "a0015c74-06ce-4905-ab9d-5a7930145cce",
    "64cd5da46ab6c2c899d1ffd1": "c89ff951-a57d-471f-8149-b791f4679dc5",
    "64cd580a6ab6c2c899d1ff37": "de14fb5e-ba32-4f08-b69a-5a0722a81ba1",
    "64ea692fd051a16d1587f575": "4c5c6ca4-e190-4bd3-b05a-b445c324a680",
    "64cd5bc16ab6c2c899d1ff9f": "55806bfc-4993-4d55-a81c-0e1dc7016b98",
    "64cd59656ab6c2c899d1ff63": "322b17d4-9f5c-404e-82c4-774e06620a72",
    "64ea6c10d051a16d1587f5db": "a0eef689-04c5-4faa-a9ae-74305164e830",
    "64cd55c56ab6c2c899d1fed3": "dd3734b1-f939-4af0-8a20-8104f60345ff",
    "6361739cfcc32170737d8627": "30100434-5a72-4b12-9836-7f2f0db67833",
    "64cd50cf6ab6c2c899d1fe2d": "e52463a7-3efa-4938-a57f-b7796430388a",
    "64cd4f696ab6c2c899d1fe17": "4fc3c5da-a928-4b88-a670-80afe057bad5",
    "64cd56b96ab6c2c899d1fef3": "d937722a-fb94-4c9b-9def-aebc7d11edb3",
    "64ea564bd051a16d1587f521": "552c548a-9fb7-41bc-9c9a-aeb3057a1cf9",
    "64ea687dd051a16d1587f547": "d799c1e1-55ff-4f0f-9777-b68338796324",
}

mongodb_postgresql_workouts_map = {
    "64ea716ad051a16d1587f61f": "4ae8cd2f-d06b-4d0f-8e50-619aa26485e3",
    "64ea866bd051a16d1587fa0a": "2640c6de-386b-4474-8bfa-f1d4eb8c4d52",
    "64ea88fdd051a16d1587fcca": "744390dc-f86e-47fc-9c45-c8bac3c168d8",
    "64ea7e19d051a16d1587f941": "a862a267-ee20-4575-b169-bc073b1be9ae",
    "64ea87e6d051a16d1587fbe0": "18eb35e8-2b69-412d-a60c-6322d916287e",
    "64ea7366d051a16d1587f758": "4b8da811-5d52-45e8-b9ea-ade2c0030728",
    "64ea7643d051a16d1587f810": "a1715eb8-dfd2-44b3-b446-35305459968c",
    "64ea9106d051a16d1587fe09": "e251aa14-b65c-43f0-92d7-0a173d47c28c",
    "64ea7effd051a16d1587f9ca": "8456c06a-61fb-44d3-8980-d510b41f9957",
    "64ea7cced051a16d1587f86f": "84fa4f2c-6094-4d58-a68e-9363757897f7",
    "64ea7ea2d051a16d1587f983": "9c47a99b-e9bc-4c59-b0a0-0e4260ef939a",
    "64ea7504d051a16d1587f7be": "042d0de7-7fb9-413e-9a7e-b99139198b0a",
    "64ea8875d051a16d1587fc59": "fd52198e-1179-471b-8618-434a44f837db"
}

mongodb_postgresql_programs_map = {
    "64ea9207d051a16d1587fe70": "7402521b-1668-4197-9284-b18f1dcf9488",
    "64eaad72d051a16d15880def": "ed8cd549-12da-4fd7-af23-3703f61bc506",
    "64eaaab5d051a16d1588027b": "24dbeaa4-e403-46a6-8027-b914c321f9db",
    "64eaabcbd051a16d15880329": "47d452f0-1f8c-4d7e-8644-281247aa4e8a",
    "64eaaca5d051a16d15880a1c": "6208fd9c-f477-4ddb-b57c-eac1813795ca",
    "64eaab58d051a16d15880305": "29153473-448f-484a-9c4e-d363d1c3e968"
}


def parse_workout_exercise_routines(json_file_path):
    with open(json_file_path, 'r') as f:
        workouts = json.load(f)

    sql_statements = []
    for workout in workouts:
        workout_id = mongodb_postgresql_workouts_map[workout['_id']['$oid']]
        for exercise in workout['exercises']:
            exercise_id = mongodb_postgresql_exercises_map[exercise['exercise']['$oid']]
            min_sets, max_sets = exercise['sets']
            min_reps, max_reps = exercise['reps']
            tempo_eccentric, tempo_pause_1, tempo_concentric, tempo_pause_2 = exercise['tempo']
            min_rir, max_rir = exercise['rir']
            superset = False
            sql = f"""
            INSERT INTO public.fitness_workoutexerciseroutine
            (id, min_sets, max_sets, min_reps, max_reps, tempo_eccentric, tempo_pause_1, tempo_concentric, tempo_pause_2, min_rir, max_rir, superset, exercise_id, superset_exercise_id, workout_id)
            VALUES
            (gen_random_uuid(), {min_sets}, {max_sets}, {min_reps}, {max_reps}, {tempo_eccentric}, {tempo_pause_1}, {tempo_concentric}, {tempo_pause_2}, {min_rir}, {max_rir}, {superset}, '{exercise_id}', null, '{workout_id}');
            """
            sql_statements.append(sql)

    # Save SQL statements to a file
    with open('fitness_workoutexerciseroutine_parsed.sql', 'w') as f:
        f.write('\n'.join(sql_statements))


def parse_program_workout_routines(json_file_path):
    with open(json_file_path, 'r') as f:
        programs = json.load(f)

    sql_statements = []
    for program in programs:
        program_id = mongodb_postgresql_programs_map[program['_id']['$oid']]
        for workout in program['workouts']:
            workout_id = mongodb_postgresql_workouts_map[workout['workout']['$oid']]
            day_of_the_week = workout['dayOfTheWeek'] if 'dayOfTheWeek' in workout else None
            day_number = workout['dayNumber'] if 'dayNumber' in workout else None
            sql = f"""
            INSERT INTO public.fitness_programworkoutroutine
            (id, sequence, day_number, day_of_the_week, program_id, workout_id)
            VALUES
            (gen_random_uuid(), '{program['sequence']}', {day_number}, '{day_of_the_week}', '{program_id}', '{workout_id}');
            """
            sql_statements.append(sql)

    # Save SQL statements to a file (appending to the existing file)
    with open('fitness_programworkoutroutine_parsed.sql', 'a') as f:
        f.write('\n'.join(sql_statements))


# Call the function with the path to your JSON file
# parse_workout_exercise_routines('/ensaludoptimadb_beta.activities.workouts.json')
parse_program_workout_routines('/ensaludoptimadb_beta.activities.programs.json')
