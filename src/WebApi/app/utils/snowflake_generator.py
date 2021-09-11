import time
import asyncio

SLEEP_DURATION = 5e-3  # 5 ms sleep

class SnowflakeGenerator:
    incrementer = 0  # max allowed is 1 << 12, or 4095
    machine_id = 12  # max allowed is 1 << 5, or 63
    process_id = 15  # max allowed is 1 << 5, or 63

    machine_id_bitmask = machine_id << 17  # consumes snowflake bits: 21 to 17
    process_id_bitmask = process_id << 12  # consumes snowflake bits: 16 to 12

    last_current_millis = time.time_ns() // 1_000_000

    async def generate_snowflake(self):
        current_millis = await self._get_valid_milliseconds()

        self.incrementer += 1
        if self.incrementer >= 4096:
            self.incrementer = 0

        # consumes snowflake bits 63 to 22
        current_millis_bitmask = current_millis << 22

        # incrementer consumes snowflake bits 11 to 0
        snowflake = current_millis_bitmask | self.machine_id_bitmask | self.process_id_bitmask | self.incrementer

        return snowflake

    async def _get_valid_milliseconds(self):
        current_millis = time.time_ns() // 1_000_000

        # Guards to make sure we don't generate multiple ids in the same millisecond or go back in time due to NTP
        if self.last_current_millis >= current_millis:
            await asyncio.sleep(SLEEP_DURATION)
            return self._get_valid_milliseconds()

        self.last_current_millis = current_millis
        return current_millis

async def test_snowflake_generation():
    generator = SnowflakeGenerator()
    snowflake = await generator.generate_snowflake()

    print(snowflake)

if __name__ == '__main__':
    asyncio.run(test_snowflake_generation())
