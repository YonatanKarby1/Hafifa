from yk_apis import WavProcessor, yk_APIRunner

if __name__ == "__main__":
    processor = WavProcessor()
    yk_apirunner = yk_APIRunner(port=8080, hostname="0.0.0.0")
    yk_apirunner.add_api_processor([processor])
    yk_apirunner.run_api()