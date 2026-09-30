MZS Oxygen Measurements
============================================================================================================================

This dataset contains oxygen measurements from Antarctic glacier ice, cryoconite, soil, and water samples collected during 
the DORMANT/SIESTA field campaign in Northern Victoria Land, Antarctica, during the austral summer 2025/26.

Oxygen measurements were conducted under light and dark incubation conditions using 20 mL PreSens sensor vials and a PreSens 
Fibox4 Oxygen Meter to assess changes in oxygen concentration associated with microbial activity.

Sample collection period: 2025-12-06/2026-01-22

> Data file: 

File name: MZS_O2.csv

The dataset contains sample identifiers and types, incubation conditions, temperature, elapsed time, replicate and sensor 
information, individual oxygen measurements, calculated means and errors, and relevant experimental observations.
Measurement positions depend on sample type: 

Sample type		Type ID			Measurement positions
-----------------------------------------------------------------------
Ice			ICE 			MID
Cryoconite		CCO			MID
Water 			WATER			BOTTOM + MID + TOP
Dry soil		DRY_SOIL		BOTTOM + MID
Wet soil		WET_SOIL		BOTTOM + MID
-----------------------------------------------------------------------

> Description of variables:

Column			Definition							Values/[Units]
----------------------------------------------------------------------------------------------------------------------------
sample_id		DORMANT field identifier					Free text
sample_type		Material incubated 						ICE, CCO, WATER, DRY_SOIL, WET_SOIL
condition		Incubation illumination condition				Light, Dark
sample_temperature	Temperature of sample						[°C]
air_temperature		Air temperature of exterior					[°C]
elapsed_time		Time since beginning of incubation				[h]
measurement_datetime	Date/time oxygen measurement was made				ISO 8601: 'yyyy-mm-ddThh:mm:ssZ'
vial_id			Incubation vial identifier					Integer
replicate		Independent incubation replicate				Integer
sensor_id		Identifier of PreSens sensor spot				Free text
o2_bottom_#		Individual technical oxygen reading at sensor position (bottom)	[%]
o2_bottom_mean		Arithmetic mean of three readings (bottom)			[%]
o2_bottom_sd		Sample standard deviation of technical readings (bottom)	[%]
o2_mid_#		Individual technical oxygen reading at sensor position (mid)	[%]
o2_mid_mean		Arithmetic mean of three readings (mid)				[%]
o2_mid_sd		Sample standard deviation of technical readings (mid)		[%]
o2_top_#		Individual technical oxygen reading at sensor position (top)	[%]
o2_top_mean		Arithmetic mean of three readings (top)				[%]
o2_top_sd		Sample standard deviation of technical readings (top)		[%]
notes			Relevant experimental observations				Free text
----------------------------------------------------------------------------------------------------------------------------

Blank cell code: 'N/M' - not measured; 'N/A' - not applicable.

> Sample identifiers (DORMANT field identifier):

Sample ID		Sample description
---------------------------------------------------------------------
MZS25_001		Glacier surface ice, Strandline Glacier
MZS25_002		Surface soil, Tarn Flat
MZS25_003		Cryoconite, Hells Gate Ice Shelf
MZS25_004		Cryoconite, Nansen Ice Shelf
MZS25_005		Glacier surface ice, Nansen Ice Shelf
MZS25_006		Surface soil, Simpson Crags
MZS25_007		Glacier surface snow, Drygalski Ice Tongue
MZS25_008		Surface soil, Random Hills Outcrop
MZS25_009		Supraglacial lake water, Priestley Glacier
MZS25_015		Surface soil, Baker Rocks
---------------------------------------------------------------------

> Analysis

Data processing and analysis code: https://github.com/drmartinezrabert/data_processing (v1.0.1)
