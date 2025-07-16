// src/app/page.tsx

import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          Iot based remote monitoring of utility parameters
        </h1>
        <p className="text-gray-600 mb-10">
          Monitor and predict key operational insights including emissions, equipment faults,
          filter clogging, and tank overfilling—all in one place.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card>
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold mb-2">🌱 Emission Prediction</h2>
              <p className="text-gray-600 mb-4">Forecast greenhouse gas emissions using utility parameters.</p>
              <Link href="/dashboard/emission">
                <Button className="w-full">View</Button>
              </Link>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold mb-2">🛠 Fault Detection</h2>
              <p className="text-gray-600 mb-4">Identify early faults in pumps and motors using voltage and vibration data.</p>
              <Link href="/dashboard/faults">
                <Button className="w-full">View</Button>
              </Link>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold mb-2">🧼 Filter Clogging</h2>
              <p className="text-gray-600 mb-4">Detect clogging in filtration equipment using pressure trends.</p>
              <Link href="/dashboard/clogging">
                <Button className="w-full">View</Button>
              </Link>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold mb-2">🛢 Tank Overfill</h2>
              <p className="text-gray-600 mb-4">Predict tank overfilling based on level and flow data.</p>
              <Link href="/dashboard/tanks">
                <Button className="w-full">View</Button>
              </Link>
            </CardContent>
          </Card>
        </div>
      </div>
    </main>
  );
}
