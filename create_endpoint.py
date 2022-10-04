import asyncio
import argparse

from trainml.trainml import TrainML

parser = argparse.ArgumentParser(
    description="Regional Classification Endpoint"
)

parser.add_argument(
    "reservation_id",
    type=str,
    help="Regional reservation ID of the port to listen on",
)

parser.add_argument(
    "port",
    type=str,
    help="The port to listen on (must match the reservation port)",
)


async def create_endpoint(trainml, reservation_id, port):
    job = await trainml.jobs.create(
        "Regional Classification Endpoint",
        type="endpoint",
        gpu_types=["gtx1060"],
        gpu_count=1,
        disk_size=10,
        endpoint=dict(
            start_command="./start_endpoint.sh", reservation_id=reservation_id
        ),
        # model=dict(
        #     source_type="git",
        #     source_uri="git@github.com:trainML/regional-endpoint-example.git",
        # ),
        model=dict(
            source_type="local",
            source_uri="~/Documents/trainML/regional-endpoint-example",
        ),
        environment=dict(
            type="DEEPLEARNING_PY39",
            packages=dict(apt=["nginx"]),
            env=[dict(key="PORT", value=port)],
        ),
    )
    return job


if __name__ == "__main__":
    args = parser.parse_args()
    trainml = TrainML()
    job = asyncio.run(create_endpoint(trainml, args.reservation_id, args.port))
    asyncio.run(job.wait_for("waiting for data/model download"))
    asyncio.run(job.connect())
    asyncio.run(job.wait_for("running"))
    asyncio.run(job.disconnect())
    print("Job ID: ", job.id, " Running")
